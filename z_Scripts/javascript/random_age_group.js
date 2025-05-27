function random_age_group_gen(){
    // Weights for each race (higher weights mean higher probability)
    const age_group_dict = {
    'Young Adult': 30,
    'Adult': 40,
    'Middle Aged': 20,
    'Senior': 10
    };
    
    // Calculate the total weight
    const totalWeight = Object.values(age_group_dict).reduce((acc, weight) => acc + weight, 0);

    // Generate a random number between 0 and the total weight
    const randomNum = Math.random() * totalWeight;

    // Choose the race based on the weighted random number
    let currentWeight = 0;
    for (const [age, weight] of Object.entries(age_group_dict)) {
        currentWeight += weight;
        if (randomNum <= currentWeight) {
            console.log("Got <" + age + "> with a chance of %" + (weight/totalWeight*100.0).toString());
            return age;
        }
    }

    // Fallback in case of unexpected conditions
    console.log("Defaulted to Adult");
    return 'Adult';
}
module.exports = random_age_group_gen;