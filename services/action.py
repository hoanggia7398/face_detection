from PIL import Image, ImageDraw
import face_recognition
import numpy as np
# import base64
import cv2


def detectImage(imageToDetect):
    print("go to detect")
    img = imageToDetect

    unknown_image = face_recognition.load_image_file(img)
    print('start')

    face_locations = face_recognition.face_locations(unknown_image,
                                                     model='cnn')
    print('flag 0')
    face_encodings = face_recognition.face_encodings(unknown_image,
                                                     face_locations)

    print("I found {} face(s) in this photograph.".format(len(face_locations)))

    dong_face_image = face_recognition.load_image_file("dong.jpg")
    print('flag 1')
    dong_face_encoding = face_recognition.face_encodings(dong_face_image)[0]
    print('flag 2')
    #gia
    gia_face_image = face_recognition.load_image_file("gia3.jpg")
    gia_face_encoding = face_recognition.face_encodings(gia_face_image)[0]

    #create encoding face and their name
    known_face_encodings = [dong_face_encoding, gia_face_encoding]
    known_face_names = ["Viet Dong", "Hoang Gia"]

    print("recognize success {} man".format(len(known_face_encodings)))

    #draw face
    pil_image = Image.fromarray(unknown_image)
    draw = ImageDraw.Draw(pil_image)

    for (top, right, bottom,
         left), face_encoding in zip(face_locations, face_encodings):

        matches = face_recognition.compare_faces(known_face_encodings,
                                                 face_encoding,
                                                 tolerance=0.42)

        # print(matches)
        name = "Unknown"

        face_distances = face_recognition.face_distance(
            known_face_encodings, face_encoding)
        # print("face distance {}".format(face_distances))

        best_match_index = np.argmin(face_distances)
        # print(best_match_index)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # Draw a box around the face using the Pillow module
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0))

        # Draw a label with a name below the face
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)),
                       fill=(0, 0, 255),
                       outline=(0, 255, 0))
        draw.text((left + 6, bottom - text_height - 5),
                  name,
                  fill=(255, 255, 255, 255))
    pil_image.show()

    # my_string = base64.b64encode(pil_image.tobytes())

    return "thanh cong"
