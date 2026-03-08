async function getRecommendations() {

    const userId = document.getElementById("userId").value

    const response = await fetch(`http://127.0.0.1:8000/recommend/${userId}`)

    const data = await response.json()

    const results = document.getElementById("results")

    results.innerHTML = ""

    data.recommendations.forEach(movie => {

        const card = document.createElement("div")

        card.className = "movie-card"

        card.innerHTML = `
<img src="https://via.placeholder.com/300x450">
<div class="movie-title">${movie}</div>
`

        results.appendChild(card)

    })

}