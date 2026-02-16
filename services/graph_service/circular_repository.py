from services.graph_service.neo4j_client import Neo4jClient


class CircularRepository:
    def __init__(self):
        self.client = Neo4jClient()

    def create_circular(self, circular_data: dict):
        query = """
        MERGE (c:Circular {circular_id: $circular_id})
        SET c.title = $title,
            c.regulator = $regulator,
            c.date = date($date),
            c.department = $department,
            c.regulation_type = $regulation_type,
            c.summary = $summary,
            c.pdf_url = $pdf_url,
            c.risk_score = $risk_score,
            c.schema_version = $schema_version,
            c.updated_at = datetime()
        RETURN c
        """

        return self.client.execute_query(query, circular_data)

    def link_industries(self, circular_id: str, industries: list):
        query = """
        MATCH (c:Circular {circular_id: $circular_id})
        UNWIND $industries AS industry_name
        MERGE (i:Industry {name: industry_name})
        MERGE (c)-[:APPLIES_TO]->(i)
        """

        return self.client.execute_query(query, {
            "circular_id": circular_id,
            "industries": industries
        })

    def link_amendment(self, new_id: str, old_id: str):
        query = """
        MATCH (new:Circular {circular_id: $new_id})
        MATCH (old:Circular {circular_id: $old_id})
        MERGE (new)-[:AMENDS]->(old)
        """

        return self.client.execute_query(query, {
            "new_id": new_id,
            "old_id": old_id
        })
    
    def link_deadline(self, circular_id: str, deadline_data: dict):
        query = """
        MATCH (c:Circular {circular_id: $circular_id})
        CREATE (d:Deadline {
            date: date($date),
            description: $description,
            urgency_score: $urgency_score
        })
        MERGE (c)-[:HAS_DEADLINE]->(d)
        """
        return self.client.execute_query(query, {
            "circular_id": circular_id,
            "date": deadline_data["date"],
            "description": deadline_data["description"],
            "urgency_score": deadline_data["urgency_score"]
        })


    def link_penalty(self, circular_id: str, penalty_data: dict):
        query = """
        MATCH (c:Circular {circular_id: $circular_id})
        CREATE (p:PenaltyClause {
            severity_level: $severity_level,
            description: $description,
            penalty_weight: $penalty_weight
        })
        MERGE (c)-[:HAS_PENALTY]->(p)
        """
        return self.client.execute_query(query, {
            "circular_id": circular_id,
            "severity_level": penalty_data["severity_level"],
            "description": penalty_data["description"],
            "penalty_weight": penalty_data["penalty_weight"]
        })

