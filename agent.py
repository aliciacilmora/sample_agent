import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="google.adk")

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from data import (
    mock_forward_shipments_db,
    mock_reverse_shipments_db,
    mock_ndr_shipments_db,
    mock_exchange_shipments_db
)

llm = LiteLlm(model="ollama_chat/llama3.2")

def get_shipment_details(awb_id: str) -> dict:
    """Retrieves full history for a specific AWB ID (NDR, Returns, Exchanges)."""
    awb_id = awb_id.upper().strip()
    if awb_id not in mock_forward_shipments_db:
        return {"status": "error", "message": f"ID {awb_id} not found."}

    return {
        "status": "success",
        "basic": mock_forward_shipments_db[awb_id],
        "ndr": next((v for v in mock_ndr_shipments_db.values() if v['original_awb'] == awb_id), None),
        "return": next((v for v in mock_reverse_shipments_db.values() if v['original_awb'] == awb_id), None),
        "exchange": next((v for v in mock_exchange_shipments_db.values() if v['original_awb'] == awb_id), None)
    }

def search_shipments_by_customer(customer_name: str) -> dict:
    """Search for shipments using the customer's name. Use this when AWB ID is unknown.
    
    Args:
        customer_name (str): The full or partial name of the customer.
    """
    results = [
        {"awb": k, "details": v} 
        for k, v in mock_forward_shipments_db.items() 
        if customer_name.lower() in v['customer'].lower()
    ]
    return {"status": "success", "found": results} if results else {"status": "error", "message": "No customer found."}

def list_shipments_by_status(status_query: str) -> dict:
    """Lists IDs matching a status (Exchanged, Delivered, RTO_Initiated)."""
    matches = [k for k, v in mock_forward_shipments_db.items() if v['status'].lower() == status_query.lower()]
    return {"status": "success", "awb_list": matches}

root_agent = Agent(
    name="logistics_agent",
    model=llm,
    description="Senior Logistics Assistant for order tracking and issue resolution.",
    instruction=(
        "1. Greet the user politely and introduce yourself as the Logistics Agent From Rusteze. "
        "2. If a user provides a name, use 'search_shipments_by_customer'. "
        "3. If a user provides an ID, use 'get_shipment_details'. "
        "4. If a shipment is RTO, always explain why (NDR issue) and the number of attempts. "
        "5. If a question is vague (e.g., 'What happened to my order?'), ask them for their name or AWB ID."
    ),
    tools=[get_shipment_details, search_shipments_by_customer, list_shipments_by_status],
)