import os
from supabase import create_client, Client
from dotenv import load_dotenv
from faker import Faker
import random

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
faker = Faker()

def get_connection():
    """
    Returns the Supabase client.
    Equivalent of a DB connection object for compatibility.
    """
    return supabase

def get_top_managers(top_n=3):
    """Fetch top N managers by total sanction amount"""
    response = (
        supabase.table("creditinfo")
        .select("credit_manager, sanction_amount")
        .execute()
    )

    data = response.data or []

    totals = {}
    for row in data:
        manager = row["credit_manager"]
        amount = float(row["sanction_amount"])
        totals[manager] = totals.get(manager, 0) + amount

    sorted_totals = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    return sorted_totals[:top_n]


def get_company_totals():
    """Fetch total company sanctions"""
    response = (
        supabase.table("creditinfo")
        .select("sanction_amount")
        .execute()
    )
    rows = response.data or []

    total_sanctions = sum(float(r["sanction_amount"]) for r in rows)
    company_target = int(total_sanctions * 1.2) if total_sanctions > 0 else 1500

    return total_sanctions, company_target


def insert_customer_record(credit_manager, customer_name, sanction_amount):
    """Insert one customer sanction record"""

    row = {
        "credit_manager": credit_manager,
        "customer_name": customer_name,
        "sanction_amount": sanction_amount,
    }

    response = supabase.table("creditinfo").insert(row).execute()
    return response.data


def upsert_fake_records(n=5):
    """Create n fake credit manager customer sanction records"""
    records = []

    managers = ["Arjun", "Riya", "Karan", "Meera", "Vikram"]

    for _ in range(n):
        record = {
            "credit_manager": random.choice(managers),
            "customer_name": faker.name(),
            "sanction_amount": round(random.uniform(50000, 500000), 2),
        }
        records.append(record)

    response = supabase.table("creditinfo").upsert(records).execute()
    return response.data

