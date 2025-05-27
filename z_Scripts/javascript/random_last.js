function random_last_gen(){
    const lastNames = [
        'Blackthorn', 'Crestfall', 'Dunewind', 'Ebonheart', 'Frostbane', 'Galewind', 'Hawkshadow', 'Ironhammer', 'Jadefire', 'Kingsbane',
        'Lionheart', 'Moonshadow', 'Nightshade', 'Oakenshield', 'Phoenixfire', 'Quicksilver', 'Ravenwing', 'Stormbreaker', 'Thunderheart', 'Underhill',
        'Valewalker', 'Windrider', 'Xanadu', 'Yewshade', 'Zephyrblade', 'Ashwood', 'Briarwood', 'Copperfield', 'Dusktreader', 'Emberheart',
        'Frostwolf', 'Goldenleaf', 'Hollowshade', 'Ironclad', 'Jewelsong', 'Kindleflame', 'Lorekeeper', 'Mistwalker', 'Nighthawk', 'Oakenshield',
        'Proudfoot', 'Quickstep', 'Ravencrest', 'Silverthorn', 'Truestrike', 'Umbrawind', 'Violetshade', 'Winterhaven', 'Xenith', 'Yewshadow',
        'Zephyrcrest', 'Anderson', 'Baker', 'Carter', 'Davis', 'Edwards', 'Fisher', 'Garcia', 'Hill', 'Irwin', 'Johnson',
        'Keller', 'Lopez', 'Morgan', 'Nelson', 'Owens', 'Parker', 'Quinn', 'Reyes', 'Smith', 'Taylor',
        'Upton', 'Vargas', 'Walker', 'Xavier', 'Yates', 'Zimmerman', 'Armstrong', 'Beckett', 'Chandler', 'Dunham', 'Everett',
        'Fletcher', 'Goldman', 'Harrison', 'Ingram', 'Jenkins', 'Kendall', 'Lawrence', 'Montgomery', 'Nash', 'O\'Donnell', 'Palmer',
        'Quigley', 'Rutherford', 'Sinclair', 'Thompson', 'Underwood', 'Van Dyke', 'Watson', 'Xander', 'Yarbrough', 'Zane',
        'Adams', 'Barnes', 'Cox', 'Dixon', 'Elliott', 'Ferguson', 'Gibson', 'Henderson', 'Ingram', 'Jennings', 'Kingsley',
        'Lawson', 'Morton', 'Nolan', 'Osborne', 'Perry', 'Quinn', 'Reeves', 'Stewart', 'Tucker', 'Underhill',
        'Vaughn', 'Wells', 'Xavier', 'Yates', 'Zimmerman', 'Abbott', 'Baxter', 'Conway', 'Davenport', 'Eldridge', 'Fairchild',
        'Gallagher', 'Harrington', 'Ingram', 'Jefferson', 'Kingsley', 'Lawson', 'McAllister', 'Nightingale', "O'Donnell", 'Parrish', 'Quintana',
        'Riley', 'Stanton', 'Thorne', 'Underwood', 'Vanderbilt', 'Watkins', 'Xavier', 'Yates', 'Zimmerman', 'Bishop', 'Cunningham',
        'Dunlop', 'Elliott', 'Fairfax', 'Galloway', 'Hollis', 'Inglewood', 'Jamison', 'Kinsley', 'Lancaster', 'Maxwell', 'Nightingale',
        'Oswald', 'Pendleton', 'Quincy', 'Rutherford', 'Sullivan', 'Thatcher', 'Upton', 'Vaughan', 'Winthrop', 'Xander', 'York',
        'Zephyr', 'Allard', 'Bancroft', 'Calloway', 'Dunbar', 'Eastwood', 'Fairchild', 'Gallagher', 'Hawthorne', 'Ingram', 'Jennings',
        'Kingsley', 'Lancaster', 'Maxwell', 'Nightingale', 'Oswald', 'Pendleton', 'Quincy', 'Rutherford', 'Sullivan', 'Thatcher', 'Upton',
        'Vaughan', 'Winthrop', 'Xander', 'York', 'Zephyr', 'Abernathy', 'Buchanan', 'Carmichael', 'Dunmore', 'Easton', 'Falkirk',
        'Glasgow', 'Harrington', 'Inverness', 'Jamison', 'Kensington', 'Lancaster', 'Montgomery', 'Northumberland', 'Oswald', 'Pendleton', 'Quincy',
        'Rutherford', 'Stirling', 'Thorne', 'Underhill', 'Victoria', 'Wycliffe', 'Xander', 'York', 'Zephyr', 'Archer', 'Bridger',
        'Chancellor', 'Dunhill', 'Evershade', 'Fairchild', 'Galloway', 'Harrington', 'Inglewood', 'Jennings', 'Kingsley', 'Lancaster', 'Maxwell',
        'Nightingale', 'Oswald', 'Pendleton', 'Quincy', 'Rutherford', 'Sullivan', 'Thatcher', 'Upton', 'Vaughan', 'Winthrop', 'Xander', 'York',
        'Zephyr'
    ];
    console.log("Generating a random last name from list of length: " + lastNames.length.toString());
    const randomIndex = Math.floor(Math.random() * lastNames.length);
    return lastNames[randomIndex];
}
module.exports = random_last_gen;