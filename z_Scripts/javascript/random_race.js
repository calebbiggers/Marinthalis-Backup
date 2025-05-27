function random_race_gen(){
    // Weights for each race (higher weights mean higher probability)
    const weight_dict = {
    'Human': 50,
    'Elf': 10,
    'Dwarf': 10,
    'Halfling': 10,
    'Gnome': 10,
    'Half-Elf': 3,
    'Half-Orc': 2,
    'Tiefling': 1,
    'Dragonborn': 1,
    'Loxodon': 1,
    'Goliath':1,
    'Tabaxi': 1
    };
    
    // Calculate the total weight
    const totalWeight = Object.values(weight_dict).reduce((acc, weight) => acc + weight, 0);

    // Generate a random number between 0 and the total weight
    const randomNum = Math.random() * totalWeight;

    // Choose the race based on the weighted random number
    let currentWeight = 0;
    for (const [race, weight] of Object.entries(weight_dict)) {
        currentWeight += weight;
        if (randomNum <= currentWeight) {
            console.log("Got <" + race + "> with a chance of %" + (weight/totalWeight*100.0).toString());
            return '"[[' + race + ']]"';
        }
    }

    // Fallback in case of unexpected conditions
    console.log("Defaulted to Human");
    return '"[[Human]]"';
}
module.exports = random_race_gen;