import geopandas as gpd
class Convert():
    def __init__(self):
        print("It is map converter.")

    def shapeToJson(self, path):

        # 读取 Shapefile
        gdf = gpd.read_file(path)

        # 替换为你希望保存的 GeoJSON 文件路径
        output_geojson_path = '../media/output.geojson'

        # 将数据保存为 GeoJSON
        gdf.to_file(output_geojson_path, driver='GeoJSON')


