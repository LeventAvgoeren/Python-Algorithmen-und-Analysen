def onehot(data,classes):
    hotList=[]  #erstelle liste
    for numbers in data:
        listVector= [0]*classes  #erstelle vektor mit gewünschten nullen
        listVector[numbers]=1  #gewünschte stelle wird mit 1 inizalisiert
        hotList.append(listVector)
    return hotList


def reshape(data, row, col):
    if len(data) != row * col:
        raise ValueError("The total number of elements does not match the desired shape.")
    
    reshaped_list = []
    for i in range(row):
        start_index = i * col  # Berechne den Start- und Endindex für das aktuelle Slice
        end_index = start_index + col
        reshaped_list.append(data[start_index:end_index])  # Füge das Slice der ursprünglichen Liste zur Ergebnisliste hinzu
    
    return reshaped_list

