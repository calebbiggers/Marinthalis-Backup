module.exports = function(item){
    ITEM_ICONS = {
        "Weapon": "LiSwords",
        "Armor": "RaVest",
        "Wondrous Item": "LiComponent",
        "Potion": "LiFlaskRound",
        "Scroll": "LiScrollText",
        "Staff": "RaCrystalWand",
        "Wand": "LiWand",
        "Rod": "LiWand2",
        "Ring": "LiComponent",
        "Shield": "LiShield"
    };
    return ITEM_ICONS[item];
}