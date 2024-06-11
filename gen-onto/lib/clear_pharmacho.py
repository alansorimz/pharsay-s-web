from owlready2 import get_ontology, destroy_entity

def delete_individual():
    ontology_path = "Pharmacho.owl"
    ontology = get_ontology(ontology_path).load()

    with ontology:
        for individual in list(ontology.individuals()):
            destroy_entity(individual)

    ontology.save(file=ontology_path)
