document.addEventListener("DOMContentLoaded", () => {

    const modals = {
        error: document.getElementById("errorModal"),
        success: document.getElementById("successModal"),
        pdf: document.getElementById("pdfModal")
    };

    const modalClosers = document.querySelectorAll(".modal .close");
    const errorTableBody = document.querySelector("#errorTable tbody");
    const pdfTableBody = document.querySelector("#pdfTable tbody");

    function showModal(type) {
        const modal = modals[type];
        modal.classList.remove("hidden");
        modal.style.display = "flex"; 
    }

    function hideModal(type) {
        modals[type].classList.add("hidden");
        modals[type].style.display = "none";
    }

    function showErrorModal(errors) {
        errorTableBody.innerHTML = "";
        let errorMap = {};

        // Agrupar errores por fila
        errors.forEach(({ fila, columna, error }) => {
            if (!errorMap[fila]) {
                errorMap[fila] = { fila, columnas: {} };
            }
            errorMap[fila].columnas[columna] = error;
        });

        Object.values(errorMap).forEach(({ fila, columnas }) => {
            let row = `<tr>
                <td>${fila}</td>
                <td>${columnas["1"] || "-"}</td>
                <td>${columnas["2"] || "-"}</td>
                <td>${columnas["3"] || "-"}</td>
                <td>${columnas["4"] || "-"}</td>
                <td>${columnas["5"] || "-"}</td>
            </tr>`;
            errorTableBody.innerHTML += row;
        });

        showModal("error");
    }

    function showSuccessModal() {
        showModal("success");
    }

    function showPdfModal(data) {
        pdfTableBody.innerHTML = "";
        data.datos.forEach(({ nombre, paginas, cufe = "No encontrado", peso }) => {
            let row = `<tr>
                <td>${nombre}</td>
                <td>${paginas}</td>
                <td>${cufe}</td>
                <td>${peso} bytes</td>
            </tr>`;
            pdfTableBody.innerHTML += row;
        });
        showModal("pdf");
    }

    modalClosers.forEach(closeBtn => closeBtn.addEventListener("click", () => {
        closeBtn.closest(".modal").classList.add("hidden");
        closeBtn.closest(".modal").style.display = "none";
    }));

    document.addEventListener("click", ({ target }) => {
        Object.values(modals).forEach(modal => {
            if (target === modal) hideModal(Object.keys(modals).find(key => modals[key] === modal));
        });
    });

    document.getElementById("uploadCsvBtn").addEventListener("click", async () => {
    
        const fileInput = document.getElementById("csvFileInput");
        if (!fileInput.files.length) {
            console.warn("⚠️ No se seleccionó un archivo.");
            return alert("Seleccione un archivo TXT.");
        }
    
        const formData = new FormData();
        formData.append("archivo", fileInput.files[0]);
    
        try {
            const response = await fetch("http://127.0.0.1:8000/api/upload/", {
                method: "POST",
                body: formData
            });
    
            // Si la respuesta no es exitosa, intentamos leerla como texto
            if (!response.ok) {
                const errorText = await response.text();
                
                try {
                    const errorData = JSON.parse(errorText); 

                    if (errorData.errores?.length) {
                        showErrorModal(errorData.errores);
                    }
                } catch (parseError) {
                    console.error("No se pudo parsear el error como JSON:", parseError);
                }

                return;
            }
    
            // Convertimos la respuesta a JSON
            const data = await response.json();
    
            // Mostramos el modal de errores si hay errores en la respuesta
            if (data.errores?.length) {
                showErrorModal(data.errores);
            } else {
                showSuccessModal();
            }
    
        } catch (error) {
            console.error("Error en la petición:", error);
            alert("Error de conexión con el servidor.");
        }
    });

    document.getElementById("uploadPdfBtn").addEventListener("click", async () => {
        const fileInput = document.getElementById("pdfFileInput");
        if (!fileInput.files.length) return alert("Seleccione archivos PDF.");

        const formData = new FormData();
        [...fileInput.files].forEach(file => formData.append("pdfs", file));

        try {
            const response = await fetch("http://127.0.0.1:8000/api/upload-pdf/", {
                method: "POST",
                body: formData
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw errorData;
            }

            const data = await response.json();
            showPdfModal(data);
        } catch (error) {
            console.error("Error al subir PDFs:", error);
            alert("Error al subir PDFs. Verifique la consola para más detalles.");
        }
    });

    document.getElementById("fetchInvoicesBtn").addEventListener("click", async () => {
        try {
            const response = await fetch("http://127.0.0.1:8000/api/listar-facturas/");
            const data = await response.json();

            if (!response.ok) {
                return alert("Error al obtener facturas. Verifique la consola.");
            }

            showPdfModal({ datos: data.facturas });
        } catch (error) {
            console.error("Error al obtener facturas:", error);
            alert("Error al obtener facturas. Verifique la consola para más detalles.");
        }
    });
});