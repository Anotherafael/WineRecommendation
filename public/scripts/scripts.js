function onClickedRecommendation() {
    var wine = document.getElementById("uiWines");
    var recommendations = document.getElementById("uiRecommendations");
    recommendations.innerHTML = "";

    var url = "http://127.0.0.1:5050/recommend_wines";

    $.post(url, {
        wine: wine.value
    }, function (data, status) {
        for (var i in data.recommendations["WineName"]) {
            var wineName = data.recommendations.WineName[i];
            var words = wineName.split(" ");

            for (let i = 0; i < words.length; i++) {
                words[i] = words[i][0].toUpperCase() + words[i].substr(1);
            }

            wineName = words.join(" ");

            recommendations.innerHTML += wineName + "<br>";
        }
    });
}

function onPageLoad() {
    var url = "http://127.0.0.1:5050/get_wine_names";
    $.get(url, function (data, status) {
        if (data) {
            var wines = data.wines;
            var uiWines = document.getElementById("uiWines");
            $('#uiWines').empty();
            for (var i in wines) {
                var opt = new Option(wines[i]);
                $('#uiWines').append(opt);
            }
        }
    });
}

window.onload = onPageLoad;