function random_sexuality_gen(){
    // Weights for each race (higher weights mean higher probability)
    const sexuality_dict = {
    'Straight': 50,
    'Bisexual': 30,
    'Gay': 15,
    'Asexual': 5
    };
    
    // Calculate the total weight
    const totalWeight = Object.values(sexuality_dict).reduce((acc, weight) => acc + weight, 0);

    // Generate a random number between 0 and the total weight
    const randomNum = Math.random() * totalWeight;

    // Choose the race based on the weighted random number
    let currentWeight = 0;
    for (const [sexuality, weight] of Object.entries(sexuality_dict)) {
        currentWeight += weight;
        if (randomNum <= currentWeight) {
            console.log("Got <" + sexuality + "> with a chance of %" + (weight/totalWeight*100.0).toString());
            return sexuality;
        }
    }

    // Fallback in case of unexpected conditions
    console.log("Defaulted to Straight");
    return 'Straight';
}
module.exports = random_sexuality_gen;