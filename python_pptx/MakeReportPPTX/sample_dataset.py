import os
import pandas as pd
import numpy as np

# type_name
type_name = "AB123-XYZ"

# Dataset
dataset = pd.DataFrame({
    "Item":["Dataset" for i in range(4)] + ["Parameter" for i in range(6)],
    "Item_2":["Unique lots", "Unique wafers", "S-test date min", "S-test date max",
              "Unique BIN", "Unique TEST", "Process Work", "PQC", "II count", "Q-time"],
    "Value":[np.nan for i in range(10)]
})

# ML learning dataset
mllearning = pd.DataFrame({
    "Item":["Dataset"] + ["Explanatory variables" for i in range(7)],
    "Item_2":["Total data sample"] + \
            ["Total", "Equipment", "Model", "Recipe", "PQC", "II count", "Q-time"],
    "Value":[np.nan for i in range(8)]
})

# diagram
diagram = pd.DataFrame({
    "Total":["Total" for i in range(15)],
    "Y*":["Ys" for i in range(5)] + ["Yr" for i in range(7)] + ["Yl" for i in range(3)],
    "BIN":["A", "A", "A", "B", "B", "C", "C", "C", "C", "D", "E", "F", "G", "H", "H"],
    "TEST":[f"TEST{i}" for i in range(1,16)],
    "Map_classification":["Ring (**%), Center (**%), Edge (**%)" for i in range(15)],
    "Slot_dependency":["Cycle 2 (**%), Cycle 4(**%), Trend increase(**%)" for i in range(15)],
    "Importance_rank":["Rank1:AAA.BBB|CCC-DDD, Rnak2:EEE.FFF|GGG-HHH, Rnak3:III.JJJ|KKK-LLL" for i in range(15)]
})

# process flow image
#process_flow = r"C:\Users\yktkk\Desktop\DS_practice\programing\pptx\process_flow.png"
process_flow = r"../sample_graph.png"

# map
#mapim = r"C:\Users\yktkk\Desktop\DS_practice\programing\pptx\map.png"
mapim = r"../sample_picture.jpg"

# graph
#graph = r"C:\Users\yktkk\Desktop\DS_practice\programing\pptx\graph_20_6.png"
graph = r"../sample_graph.png"

# test
stat_matrix = pd.DataFrame({
    "Statistics":["Average", "Median", "Max", "Min", "Variation", "Standard deviation", "skewness", "kurtosis"],
    "Value":[np.nan for i in range(8)]
})

# condition
cond = pd.DataFrame({
    "Type":["Map Edge", "Map Ring", "Map Center", "Slot Cycle_2", "Slot Trend_increase", "Slot Bias_front"],
    "Frequency":["**%" for i in range(6)]
})

# map images
'''
map_images = pd.DataFrame({
    "Mode":["Edge", "Ring", "Center"],
    "ALL_img_paths":[mapim, mapim, mapim],
    "ALL_img_regional_paths":[mapim, mapim, mapim],
    "Sample1_lotid":["aaaaaaaa", "bbbbbbbb", "cccccccc"],
    "Samp1_img_paths":[mapim, mapim, mapim],
    "Sample2_lotid":["aaaaaaaa", "bbbbbbbb", "cccccccc"],
    "Samp2_img_paths":[mapim, mapim, mapim],
})
'''
map_images = pd.DataFrame({
    "Mode":[],
    "ALL_img_path":[],
    "ALL_img_reginal_paths":[],
    "lotid":[],
    "lot_img":[]
})
# make dataframe
modes = ["Edge", "Ring", "Center", "Random"]
for m in modes:
    for i in range(10):
        for j in range(10):
            map_images = pd.concat([
                map_images,
                pd.DataFrame({
                    "Test":[f"TEST{i}"],
                    "Mode":[m],
                    "ALL_img_path":[mapim],
                    "ALL_img_reginal_path":[mapim],
                    "lotid":["aaaaaaaa"],
                    "lot_img":[mapim],
                })
            ])
map_images["FailureRate"] = [i*0.01 for i in range(len(map_images))]
map_images.reset_index(drop=True, inplace=True)

# slot df
slot_df = pd.DataFrame({
    "Test":[],
    "Mode":[],
    "lotid":[]
})
# make dataframe
modes = ["Slot Cycle_2", "Slot Trend_increase", "Slot Bias_front", np.nan]
for m in modes:
    for i in range(10):
        for j in range(10):
            slot_df = pd.concat([
                slot_df,
                pd.DataFrame({
                    "Test":[f"TEST{i}"],
                    "Mode":[m],
                    "lotid":["aaaaaaaa"]
                })
            ])
slot_df["FailureRate"] = [i*0.01 for i in range(len(slot_df))]
slot_df.reset_index(drop=True, inplace=True)


# graph lot images
graph_lot_images = pd.DataFrame({
    "Mode":["Cycle_2", "Cycle_4", "Trend_increase"],
    "Sample1_lotid":["aaaaaaaa", "bbbbbbbb", "cccccccc"],
    "Samp1_graph_paths":[graph, graph, graph],
    "Sample2_lotid":["aaaaaaaa", "bbbbbbbb", "cccccccc"],
    "Samp2_graph_paths":[graph, graph, graph]
})

# importance
imp = pd.DataFrame({
    "Ranking":[i for i in range(1,16)],
    "Item":["Item AAA BBB" for i in range(15)],
    "Importance":[16-i for i in range(15)],
    "Accuracy":[round(1-0.2*i,2) for i in range(15)]
})

# importance graph sample
imp_graphs = pd.DataFrame({
    "Parameter":["aaaaaaaa", "bbbbbbbb", "cccccccc"],
    "graph_1":[graph, graph, graph],
    "graph_2":[graph, graph, graph]
})
