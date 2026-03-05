"""
This module serves as the mock database for the logistics agent.
It contains forward shipments, reverse shipments, NDRs, and exchanges.
"""

mock_forward_shipments_db = {
    "FWD-1001": {"date": "2023-10-01", "customer": "Aarav Patel", "status": "Delivered", "amount": 1200},
    "FWD-1002": {"date": "2023-10-01", "customer": "Vihaan Reddy", "status": "Delivered", "amount": 850},
    "FWD-1003": {"date": "2023-10-02", "customer": "Aditya Sharma", "status": "Delivered", "amount": 2100},
    "FWD-1004": {"date": "2023-10-02", "customer": "Sai Kumar", "status": "Delivered", "amount": 450},
    "FWD-1005": {"date": "2023-10-03", "customer": "Reyansh Singh", "status": "Delivered", "amount": 3200},
    "FWD-1006": {"date": "2023-10-03", "customer": "Arjun Gupta", "status": "Delivered", "amount": 1500},
    "FWD-1007": {"date": "2023-10-04", "customer": "Kiara Advani", "status": "Delivered", "amount": 900},
    "FWD-1008": {"date": "2023-10-04", "customer": "Ishaan Verma", "status": "Delivered", "amount": 2500},
    "FWD-1009": {"date": "2023-10-05", "customer": "Saanvi Mehta", "status": "Delivered", "amount": 600},
    "FWD-1010": {"date": "2023-10-05", "customer": "Ayaan Khan", "status": "Delivered", "amount": 1100},
    "FWD-1011": {"date": "2023-10-06", "customer": "Zara Siddiqui", "status": "Delivered", "amount": 3400},
    "FWD-1012": {"date": "2023-10-06", "customer": "Kabir Das", "status": "Delivered", "amount": 550},
    "FWD-1013": {"date": "2023-10-07", "customer": "Ananya Roy", "status": "RTO_Initiated", "amount": 1800},
    "FWD-1014": {"date": "2023-10-07", "customer": "Rohan Joshi", "status": "RTO_Initiated", "amount": 950},
    "FWD-1015": {"date": "2023-10-08", "customer": "Meera Nair", "status": "RTO_Initiated", "amount": 2200},
    "FWD-1016": {"date": "2023-10-08", "customer": "Dhruv Malhotra", "status": "RTO_Initiated", "amount": 300},
    "FWD-1017": {"date": "2023-10-09", "customer": "Naira Kapoor", "status": "RTO_Initiated", "amount": 4100},
    "FWD-1018": {"date": "2023-10-09", "customer": "Arnav Singh", "status": "Exchanged", "amount": 1250},
    "FWD-1019": {"date": "2023-10-10", "customer": "Pari Chopra", "status": "Exchanged", "amount": 2700},
    "FWD-1020": {"date": "2023-10-10", "customer": "Vivaan Jain", "status": "Exchanged", "amount": 890}
}

mock_reverse_shipments_db = {
    "REV-9001": {"original_awb": "FWD-1013", "return_date": "2023-10-12", "reason": "Customer Refused", "refund_status": "Processed"},
    "REV-9002": {"original_awb": "FWD-1014", "return_date": "2023-10-13", "reason": "Address Incomplete", "refund_status": "Pending"},
    "REV-9003": {"original_awb": "FWD-1015", "return_date": "2023-10-14", "reason": "Customer Not Available", "refund_status": "Processed"},
    "REV-9004": {"original_awb": "FWD-1016", "return_date": "2023-10-15", "reason": "Damaged in Transit", "refund_status": "Processed"},
    "REV-9005": {"original_awb": "FWD-1017", "return_date": "2023-10-16", "reason": "COD Amount Mismatch", "refund_status": "Pending"}
}

mock_ndr_shipments_db = {
    "NDR-501": {"original_awb": "FWD-1010", "ndr_date": "2023-10-06", "issue": "Customer Unreachable", "attempts": 1, "final_outcome": "Delivered"},
    "NDR-502": {"original_awb": "FWD-1011", "ndr_date": "2023-10-07", "issue": "Door Locked", "attempts": 2, "final_outcome": "Delivered"},
    "NDR-503": {"original_awb": "FWD-1012", "ndr_date": "2023-10-07", "issue": "Entry Restricted", "attempts": 1, "final_outcome": "Delivered"},
    "NDR-504": {"original_awb": "FWD-1013", "ndr_date": "2023-10-08", "issue": "Customer Refused", "attempts": 3, "final_outcome": "RTO"},
    "NDR-505": {"original_awb": "FWD-1014", "ndr_date": "2023-10-09", "issue": "Address Incomplete", "attempts": 3, "final_outcome": "RTO"},
    "NDR-506": {"original_awb": "FWD-1015", "ndr_date": "2023-10-10", "issue": "Customer Not Available", "attempts": 3, "final_outcome": "RTO"},
    "NDR-507": {"original_awb": "FWD-1016", "ndr_date": "2023-10-11", "issue": "Damaged in Transit", "attempts": 1, "final_outcome": "RTO"},
    "NDR-508": {"original_awb": "FWD-1017", "ndr_date": "2023-10-12", "issue": "COD Amount Mismatch", "attempts": 2, "final_outcome": "RTO"}
}

mock_exchange_shipments_db = {
    "EXC-201": {"original_awb": "FWD-1018", "exchange_date": "2023-10-12", "new_item": "Size M -> Size L", "status": "Dispatched"},
    "EXC-202": {"original_awb": "FWD-1019", "exchange_date": "2023-10-14", "new_item": "Blue -> Black", "status": "In Transit"},
    "EXC-203": {"original_awb": "FWD-1020", "exchange_date": "2023-10-15", "new_item": "Defective -> Replacement", "status": "Delivered"}
}