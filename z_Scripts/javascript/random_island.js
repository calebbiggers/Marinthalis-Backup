function random_island(){
    // Weights for each race (higher weights mean higher probability)
    const island_dict = {
    "Baldur's Gate": 1,
    "Siroccia": 1,
    "Stygia": 1,
    'Tranquil Refuge Archipelago': 1,
    "Waterdeep" : 1,
    "Random": 1
    };

    const random_islands = [
        "Serpent Isle",
        "Misthaven",
        "Isle of Whispers",
        "Tidewater Key",
        "Two Bush Reef",
        "Vaso Island",
        "North Aurora Bar",
        "Conger Rock",
        "Houseboat Point",
        "Onset Island",
        "Amber Archipelago",
        "Gravenwall",
        "Surboia",
        "Hatheim",
        "Rimbron",
        "The Colossal Isles",
        "Cardry"
    ]
    
    // Calculate the total weight
    const totalWeight = Object.values(island_dict).reduce((acc, weight) => acc + weight, 0);

    // Generate a random number between 0 and the total weight
    const randomNum = Math.random() * totalWeight;

    // Choose the race based on the weighted random number
    let currentWeight = 0;
    for (const [island, weight] of Object.entries(island_dict)) {
        currentWeight += weight;
        if (randomNum <= currentWeight) {
            console.log("Got <" + island + "> with a chance of %" + (weight/totalWeight*100.0).toString());
            if(island == "Random"){
                const randomIndex = Math.floor(Math.random() * random_islands.length);
                return '"[[' + random_islands[randomIndex] + ']]"';
            }
            return '"[[' + island + ']]"';
        }
    }

    // Fallback in case of unexpected conditions
    console.log("Defaulted to Baldur's Gate");
    return "\"[[Baldur's Gate]]\"";
}
module.exports = random_island;