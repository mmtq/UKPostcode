
document.getElementById("openModalBtn").addEventListener("click", function () {
    const searchTerm = "{{ postcode.postcode|escapejs }}";
    document.getElementById("myModal").classList.remove("hidden");
    fetch(`/api/fetch-data/?search=${encodeURIComponent(searchTerm)}`)
        .then(response => response.json())
        .then(data => {
            if (!data.error) {
                var schoolListHTML = "";

                // Loop over the array and append each item as an <li>
                for (var item of data.schools) {
                    schoolListHTML += "<li>" + item + "</li>";
                }

                document.getElementById("smodalData").innerHTML = schoolListHTML;
            } else {
                document.getElementById("modalData").innerHTML = `<p class="text-red-500">Error: ${data.error}</p>`;
            }
        })
        .catch(error => {
            document.getElementById("modalData").innerHTML = `<p class="text-red-500">Error loading data</p>`;
        });
});
document.getElementById("closeModalBtn").addEventListener("click", function () {
    document.getElementById("myModal").classList.add("hidden");
});
window.onclick = function (event) {
    var modal = document.getElementById("myModal");
    var bmodal = document.getElementById("bModal");

    if (event.target === modal) {
        modal.classList.add("hidden");
    }
    else if (event.target === bmodal) {
        bmodal.classList.add("hidden");
    }
};

document.getElementById("bopenModalBtn").addEventListener("click", function () {
    const searchTerm = "{{ postcode.postcode|escapejs }}";
    document.getElementById("bModal").classList.remove("hidden");
    fetch(`/api/fetch-data/?search=${encodeURIComponent(searchTerm)}`)
        .then(response => response.json())
        .then(data => {
            if (!data.error) {
                var busListHTML = "";

                // Loop over the array and append each item as an <li>
                for (var item of data.busStops) {
                    busListHTML += "<li>" + item + "</li>";
                }

                document.getElementById("bmodalData").innerHTML = busListHTML;
            } else {
                document.getElementById("bmodalData").innerHTML = `<p class="text-red-500">Error: ${data.error}</p>`;
            }
        })
        .catch(error => {
            document.getElementById("bmodalData").innerHTML = `<p class="text-red-500">Error loading data</p>`;
        });

});

// Close the modal
document.getElementById("bcloseModalBtn").addEventListener("click", function () {
    document.getElementById("bModal").classList.add("hidden");
});

