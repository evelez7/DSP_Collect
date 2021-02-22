import json
import GameMain

def collect_game_main():
    json_construct = {}
    top_level_attributes = dir(GameMain)
    json_construct["GameMain"] = {}
    for attribute in top_level_attributes:
        x = ""
        try:
            x = eval("GameMain."+ attribute)
        except Exception as inst:
            pass
        json_construct["GameMain"][attribute] = type(x).__name__
    with open('gameMain.json', 'w') as outfile:
        json.dump(json_construct, outfile)

def collect_galaxy():
    star_data_attributes = dir(GameMain.galaxy)
    galaxy_dict = {}
    galaxy_dict["galaxy"] = {}

    for attribute in star_data_attributes:
        x = ""
        try:
            x = eval("GameMain.galaxy." + attribute)
        except Exception as inst:
            pass
        galaxy_dict["galaxy"][attribute] = type(x).__name__
    with open('galaxy_data.json', 'w') as outfile:
        json.dump(galaxy_dict, outfile)

def collect_top_level():
    to_collect = [("localPlanet", "PlanetData"), ("instance", "GameMain"), ("mainPlayer", "Player"), ("galaxy", "GalaxyData"), ("data", "GameData"), ("gameScenario", "GameScenarioLogic"), ("history", "GameHistoryData"), ("statistics", "GameStatData"), ("localStar", "StarData"), ("preferences", "GamePrefsData"), ("universeSimulator", "UniverseSimulator"), ("mainPlayer.factory", "PlanetFactory"), ("mainPlayer.factory.dysonSphere", "DysonSphere"), ("mainPlayer.factory.cargoTraffic", "CargoTraffic"), ("mainPlayer.factory.factoryStorage", "FactoryStorage"), ("mainPlayer.factoryAudio", "FactoryAudio"), ("mainPlayer.factory.monsterSystem", "MonsterSystem"), ("mainPlayer.mecha", "Mecha"), ("mainPlayer.navigation", "PlayerNavigation"), ("mainPlayer.orders", "PlayerOrder"), ("universeSimulator.sunFlareG", "Flare"), ("universeSimulator.starPrefab", "StarSimulator"), ("localStar.type", "EStarType"), ("mainPlayer.effect", "PlayerEffect"), ("statistics.production", "ProductionStatistics")]
    for item in to_collect:
        attributes = dir(eval("GameMain."+ item[0]))
        attribute_dict = {}
        attribute_dict[item[1]] = {}

        for attribute in attributes:
            x = ""
            try:
                x = eval("GameMain." + item[0] + "." + attribute)
            except Exception as inst:
                pass
            attribute_dict[item[1]][attribute] = type(x).__name__
        with open(item[1] + ".json", 'w') as outfile:
            json.dump(attribute_dict, outfile)
def main():
    print("importing GameMain")
    print("beginning collection")
    collect_top_level()
    print("done!")