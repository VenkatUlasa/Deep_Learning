'''
Printing the count of each class of each frame.
'''

import numpy as np
import cv2

model_width , model_height = 320 , 320
video = cv2.VideoCapture("yolo_test.mp4")

thrshold = 0.5
def get_best_boxes(outcome) :
    bound_boxes = []
    cls_name_index = []
    prob_values_list = []
    for i in outcome :
        for j in i :
            prob_values = j[5:]
            cls_index = np.argmax(prob_values)
            best_value = prob_values[cls_index]

            if best_value > thrshold :
                w,h = int(j[2]*model_width) , int(j[3]*model_height)
                x, y = int(j[0]*model_width - w/2) , int(j[1]*model_width - h/2)
                bound_boxes.append([x,y,w,h])
                cls_name_index.append(cls_index)
                prob_values_list.append(best_value)

    final_boxes = cv2.dnn.NMSBoxes(bound_boxes , prob_values_list , thrshold , 0.6)
    return final_boxes , bound_boxes , cls_name_index , prob_values_list

def final_detection(final_bxs , all_boxs , indexes , values , wid , high) :
    for a in final_bxs :
        x,y,w,h = all_boxs[a]
        x = int(x * wid)
        y = int(y * high)
        w = int(w * wid)
        h = int(h * high)
        cls_name = coco_class_names[indexes[a]]

        cv2.rectangle(image , (x,y) , (w+x , h+y) , (0,0,255) , 2)
        cv2.putText(image , cls_name , (x , y-20) , cv2.FONT_HERSHEY_PLAIN , 1 , (0,0,255) , 2)


coco_class_names = []  # all the class names in coco dataset
with open("coco_names.names" , "r") as f :
    names = f.readlines()
    for i in names :
        coco_class_names.append(i.strip())

v3_network = cv2.dnn.readNetFromDarknet("yolov3.cfg" , "yolov3-weights.weights")
all_layers = v3_network.getLayerNames()
layers_index = v3_network.getUnconnectedOutLayers()
detection_layers = [all_layers[a-1] for a in layers_index]
while True :
    status , image = video.read()
    im_width , im_height = image.shape[1] , image.shape[0]
    if status == True :
        input_image = cv2.dnn.blobFromImage(image,1/255,(320,320),True,crop=False)
        v3_network.setInput(input_image)
        net_outcome = v3_network.forward(detection_layers)

        f_bxs, bo_boxs , cls_index_list , values_list = get_best_boxes(net_outcome)

        final_detection(f_bxs , bo_boxs , cls_index_list , values_list , im_width/320 , im_height/320)
        unique_classes = set(cls_index_list)
        text = ""
        for i in unique_classes :
            c = cls_index_list.count(i)
            cls = coco_class_names[i]
            text += f" {cls} : {c} "
        cv2.putText(image ,text  , (20,40) , cv2.FONT_HERSHEY_PLAIN , 2 , (0,0,0) , 3 )
        cv2.imshow("image" , image)
        if cv2.waitKey(1) == ord("q") :
            break
    else :
        break
video.release()
cv2.destroyAllWindows()