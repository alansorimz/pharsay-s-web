from flask import request, jsonify
from owlready2 import get_ontology, Thing

def insert_relation(new_onto):
    # Memuat ontologi dari file
    ontology_path = "Pharmacho.owl"
    onto = get_ontology(ontology_path).load()
    try:
        # Membaca data dari triplet
        lines = new_onto

        def get_or_create_entity(ontology, entity_name, entity_type):
            entity = getattr(ontology, entity_name, None)
            if entity is None:
                entity = type(entity_name, (entity_type,), {})
                setattr(ontology, entity_name, entity)
            return entity

        with onto:
            for line in lines:
                line = line.strip()
                if line.startswith("onto."):
                    try:
                        command = line.split(".")[1]
                        entity_name, property_command = command.split(".")[0], ".".join(command.split(".")[1:])
                        entity_type_name = property_command.split("(")[0]
                        property_name = property_command.split(".")[0]

                        entity_type = getattr(onto, entity_type_name, Thing)
                        entity = get_or_create_entity(onto, entity_name, entity_type)

                        exec(line)
                    except IndexError:
                        print(f"Skipping malformed line: {line}")
                    except Exception as e:
                        print(f"Error processing line {line}: {e}")

        onto.save(file=ontology_path)

        return {'message': 'Data has been added to ontology and saved successfully.'}

    except Exception as e:
        return {'error': str(e)}
