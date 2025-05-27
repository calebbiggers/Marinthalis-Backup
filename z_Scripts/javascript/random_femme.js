function random_femme_gen(){
    const feminineNames = [
        'Aeliana', 'Brielle', 'Cassandra', 'Dahlia', 'Elowen', 'Fiona', 'Gwendolyn', 'Hazel', 'Isolde', 'Jasmine',
        'Kira', 'Lorelei', 'Maeve', 'Nadia', 'Ophelia', 'Penelope', 'Quinna', 'Rosalind', 'Seraphina', 'Tessa',
        'Ursula', 'Vivienne', 'Willow', 'Xanthe', 'Yara', 'Zephyrine', 'Aria', 'Belle', 'Celine', 'Daisy',
        'Evangeline', 'Felicity', 'Giselle', 'Helena', 'Ivy', 'Juliet', 'Keira', 'Luna', 'Mira', 'Natalia',
        'Oriana', 'Persephone', 'Quiana', 'Rhiannon', 'Selene', 'Thalia', 'Uma', 'Violet', 'Wren', 'Xandra',
        'Yasmine', 'Zara', 'Amara', 'Brynn', 'Calista', 'Daphne', 'Elara', 'Fiora', 'Genevieve', 'Halle', 'Iris',
        'Juniper', 'Kenna', 'Lyra', 'Morgana', 'Nyx', 'Odessa', 'Pandora', 'Quincy', 'Raven', 'Soraya', 'Thea',
        'Ulyssa', 'Vespera', 'Winona', 'Xyla', 'Yvaine', 'Zinnia', 'Arabella', 'Blaise', 'Celestia', 'Dahlia',
        'Elysia', 'Freya', 'Guinevere', 'Hermione', 'Isabeau', 'Jocelyn', 'Kallista', 'Lavender', 'Maevis', 'Nerida',
        'Ondine', 'Pandora', 'Quintessa', 'Ravenna', 'Selene', 'Talitha', 'Undine', 'Violetta', 'Winslow', 'Xylia',
        'Ysolde', 'Zephyrine', 'Athena', 'Bellatrix', 'Cerelia', 'Diana', 'Elara', 'Faelan', 'Galadriel', 'Hespera',
        'Ithilwen', 'Jessamine', 'Kalliope', 'Lirael', 'Morrigan', 'Nerissa', 'Ondine', 'Phaedra', 'Quintessa', 'Roxanne',
        'Seraphia', 'Thalassa', 'Umbriel', 'Valoria', 'Winter', 'Xylona', 'Yavana', 'Zephyria', 'Acacia', 'Bianca',
        'Camille', 'Delphine', 'Eulalia', 'Faylinn', 'Gwyneth', 'Haven', 'Iliad', 'Jelena', 'Katriel', 'Lilith',
        'Marigold', 'Nimue', 'Odalys', 'Peregrine', 'Quintessa', 'Rhoswen', 'Sylvaine', 'Talise', 'Undine', 'Veridian',
        'Wisteria', 'Xandra', 'Ysabeau', 'Zephyrine', 'Adalyn', 'Briar', 'Callista', 'Della', 'Evanthia', 'Fioralba',
        'Gisella', 'Hespera', 'Irina', 'Junia', 'Kalista', 'Laelia', 'Mirella', 'Nolana', 'Orielle', 'Petrina',
        'Quinara', 'Ravenna', 'Serena', 'Talitha', 'Umbrielle', 'Valencia', 'Wynona', 'Xylara', 'Ysella', 'Zafira',
        'Amaryllis', 'Bryony', 'Calliope', 'Dysis', 'Evanora', 'Ferelith', 'Gwyneira', 'Halcyon', 'Isidora', 'Jovianne',
        'Kasiani', 'Lorella', 'Maelis', 'Neroli', 'Olwen', 'Pyrrha', 'Quenby', 'Rhoswen', 'Sylvaine', 'Thessaly',
        'Umbria', 'Valencia', 'Wrenna', 'Xylia', 'Yseult', 'Zephyrine'
    ];
    console.log("Generating a random femme name from list of length: " + feminineNames.length.toString());
    const randomIndex = Math.floor(Math.random() * feminineNames.length);
    return feminineNames[randomIndex];
}
module.exports = random_femme_gen;