// ===============================
// Student Task Manager
// JavaScript
// ===============================

console.log("✅ Student Task Manager JavaScript Loaded Successfully");

document.addEventListener("DOMContentLoaded", function () {

    console.log("✅ DOM Loaded");

    // -------------------------------
    // Delete Confirmation
    // -------------------------------

    const deleteButtons = document.querySelectorAll(".btn-danger");

    deleteButtons.forEach(button => {

        if (button.textContent.trim() === "Delete") {

            button.addEventListener("click", function (event) {

                const confirmed = confirm(
                    "Are you sure you want to delete this task?"
                );

                if (!confirmed) {
                    event.preventDefault();
                }

            });

        }

    });

});