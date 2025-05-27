function random_masc_gen(){
    const masculineNames = [
        'Alden', 'Barrett', 'Caelum', 'Desmond', 'Emery', 'Finnian', 'Garrick', 'Harlan', 'Icarus', 'Jaxon',
        'Kieran', 'Lucian', 'Malachi', 'Niall', 'Orin', 'Percival', 'Quillan', 'Rhydian', 'Soren', 'Thorne',
        'Ulric', 'Valerian', 'Wystan', 'Xander', 'Yorick', 'Zephyr', 'Alaric', 'Baelor', 'Cedric', 'Darian',
        'Emeric', 'Faustus', 'Gideon', 'Haldir', 'Isidore', 'Jorah', 'Kaelan', 'Lysander', 'Maelor', 'Nyro',
        'Orion', 'Pyrrhus', 'Quillon', 'Riven', 'Samael', 'Talon', 'Uther', 'Varian', 'Wyndham', 'Xylon',
        'Yarrow', 'Zane', 'Atlas', 'Briar', 'Cade', 'Delphine', 'Eldric', 'Fioran', 'Gavric', 'Halcyon',
        'Ilian', 'Jareth', 'Kaelum', 'Landon', 'Maelor', 'Niall', 'Osric', 'Perrin', 'Quinlan', 'Rylan',
        'Saber', 'Tavish', 'Ulysses', 'Valerian', 'Willem', 'Xanthus', 'Ymir', 'Zephyros', 'Asher', 'Beowulf',
        'Caelum', 'Declan', 'Eadric', 'Faelan', 'Gareth', 'Haldor', 'Inigo', 'Jaxton', 'Kaelan', 'Larkin',
        'Maelor', 'Nyro', 'Orik', 'Palden', 'Quillon', 'Rylan', 'Saber', 'Thorne', 'Ulric', 'Varric',
        'Zephyrion', 'Kasimir', 'Leopold', 'Roderick', 'Maximus', 'Cassius', 'Thorgrim', 'Oberon', 'Ferdinand',
        'Octavius', 'Cyrus', 'Luther', 'Balthazar', 'Benedict', 'Gareth', 'Wolfgang', 'Dmitri', 'Aurelius',
        'Remus', 'Lorenzo', 'Ignatius', 'Hector', 'Regulus', 'Leander', 'Tiberius', 'Caius', 'Alaricus', 'Augustus',
        'Horatio', 'Xerxes', 'Zephyrion', 'Tybalt', 'Osmond', 'Tarquin', 'Tycho', 'Virgil', 'Waldemar',
        'Alexander', 'Christopher', 'Daniel', 'Matthew', 'Nicholas', 'Benjamin', 'Andrew', 'Jonathan', 'William',
        'James', 'Joseph', 'Michael', 'David', 'John', 'Richard', 'Robert', 'Thomas', 'Brian', 'Patrick',
        'Jacob', 'Ethan', 'Daniel', 'Mason', 'Logan', 'Jackson', 'David', 'Joseph', 'Samuel', 'Elijah',
        'Benjamin', 'Matthew', 'James', 'Gabriel', 'Christopher', 'Andrew', 'William', 'Jonathan', 'Nathan',
        'Ryan', 'Nicholas', 'Tyler', 'Brandon', 'Cameron', 'Austin', 'Dylan', 'Kevin', 'Evan', 'Jordan'
    ];
    console.log("Generating a random masc name from list of length: " + masculineNames.length.toString());
    const randomIndex = Math.floor(Math.random() * masculineNames.length);
    return masculineNames[randomIndex];
}
module.exports = random_masc_gen;