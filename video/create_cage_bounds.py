import face_recognition
import os

# create encoding of known cage image to compare faces with
cage_image = face_recognition.load_image_file('./temp/face_recognition/to_recognise/Nicolas Cage.jpg')
cage_encoding = face_recognition.face_encodings(cage_image)[0]

# loop through downloaded images - create csv of cage face locations for cropping shell script to refer to
cage_csv = open('./temp/face_recognition/cage_bounds.csv', 'w')
column_titles = 'file_name, face_index, top, right, bottom, left'
cage_csv.write(column_titles + '\n')

for file in os.listdir('./temp/downloads'): 
    if file.endswith('.jpg'):
        image_path = os.path.join('./temp/downloads', file)
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.api.face_locations(image)
        if (len(face_locations) > 0): # if faces are detected
            # encode each face
            image_face_encodings = face_recognition.face_encodings(image, known_face_locations=face_locations)
            cage_locations = [] # list of bounding box coordinates for cage faces
            for index, encoding in enumerate(image_face_encodings):
                results = face_recognition.compare_faces([cage_encoding], encoding, tolerance=0.8)
                if (results[0] == True):
                    bounds = face_locations[index]
                    cage_csv.write('{},{},{},{},{},{}\n'.format(file, index, bounds[0], bounds[1], bounds[2], bounds[3]))