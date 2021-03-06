# -*- coding: utf-8 -*-

"""
    healthoslib.models.interaction
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 02/18/2017
"""
import healthoslib.models.item
import healthoslib.models.base_model

class Interaction(healthoslib.models.base_model.BaseModel):

    """Implementation of the 'Interaction' model.

    TODO: type model description here.

    Attributes:
        items (list of Item): TODO: type description here.
        severity (string): TODO: type description here.
        description (string): TODO: type description here.
        source (string): TODO: type description here.

    """

    def __init__(self, 
                 items = None,
                 severity = None,
                 description = None,
                 source = None):
        """Constructor for the Interaction class"""
        
        # Initialize members of the class
        self.items = items
        self.severity = severity
        self.description = description
        self.source = source

        # Create a mapping from Model property names to API property names
        self.names = {
            "items" : "items",
            "severity" : "severity",
            "description" : "description",
            "source" : "source",
        }


    @classmethod
    def from_dictionary(cls, 
                        dictionary):
        """Creates an instance of this model from a dictionary
       
        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.
            
        Returns:
            object: An instance of this structure class.
            
        """
        if dictionary == None:
            return None
        else:
            # Extract variables from the dictionary
            items = None
            if dictionary.get("items") != None:
                items = list()
                for structure in dictionary.get("items"):
                    items.append(healthoslib.models.item.Item.from_dictionary(structure))
            severity = dictionary.get("severity")
            description = dictionary.get("description")
            source = dictionary.get("source")
            # Return an object of this model
            return cls(items,
                       severity,
                       description,
                       source)


