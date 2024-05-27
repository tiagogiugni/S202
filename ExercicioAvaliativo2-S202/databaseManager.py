class Teachers:
    def __init__(self, database):
        self.db = database

    # Questão 1

    def get_professor_details(self, name):
        query = "MATCH (t:Teacher {name: $name}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        parameters = {"name": name}
        result = self.db.execute_query(query, parameters)
        return result
    
    def get_professors_starting_with_m(self):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS name, t.cpf AS cpf"
        result = self.db.execute_query(query)
        return result

    def get_all_cities(self):
        query = "MATCH (c:City) RETURN c.name AS name"
        result = self.db.execute_query(query)
        return result

    def get_schools_in_range(self):
        query = """
        MATCH (s:School)
        WHERE s.number >= 150 AND s.number <= 550
        RETURN s.name AS name, s.address AS address, s.number AS number
        """
        result = self.db.execute_query(query)
        return result
    
    #Questão 2
    
    def get_oldest_and_youngest_professor_year(self):
        query = """
        MATCH (t:Teacher)
        RETURN MAX(t.ano_nasc) AS youngest_year, MIN(t.ano_nasc) AS oldest_year
        """
        result = self.db.execute_query(query)
        return result

    def get_average_population(self):
        query = "MATCH (c:City) RETURN AVG(c.population) AS average_population"
        result = self.db.execute_query(query)
        return result

    def get_city_by_cep(self, cep):
        query = """
        MATCH (c:City {cep: $cep})
        RETURN REPLACE(c.name, 'a', 'A') AS modified_name
        """
        parameters = {"cep": cep}
        result = self.db.execute_query(query, parameters)
        return result

    def get_third_letter_from_professor_names(self):
        query = """
        MATCH (t:Teacher)
        RETURN SUBSTRING(t.name, 2, 1) AS third_letter
        """
        result = self.db.execute_query(query)
        return result
    
    # Questão 3

class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)

    def read(self, name):
        query = "MATCH (t:Teacher {name: $name}) RETURN t"
        parameters = {"name": name}
        result = self.db.execute_query(query, parameters)
        return result

    def delete(self, name):
        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def update(self, name, newCpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $newCpf RETURN t"
        parameters = {"name": name, "newCpf": newCpf}
        result = self.db.execute_query(query, parameters)
        return result
