async function loadRecommendations() {

    const userId = document.getElementById("userId").value

    const res = await fetch(`http://127.0.0.1:8000/recommend/${userId}`)

    const data = await res.json()

    renderRow("recommended", data.recommended)

    renderRow("trending", data.trending)

    renderRow("discover", data.discover)

}


async function getPoster(movie) {

    const res = await fetch(
        `http://127.0.0.1:8000/poster/${movie}`
    )

    const data = await res.json()

    if (data.poster) {

        return data.poster

    }

    return "https://via.placeholder.com/300x450"

}


async function renderRow(containerId, movies) {

    const container = document.getElementById(containerId)

    container.innerHTML = ""

    for (const movie of movies) {

        const poster = await getPoster(movie)

        const card = document.createElement("div")

        card.className = "movie-card"

        card.innerHTML = `
<img src="${poster}">
<div class="movie-title">${movie}</div>
`

        container.appendChild(card)

    }

}