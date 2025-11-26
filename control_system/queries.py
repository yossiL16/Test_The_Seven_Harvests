from control_system.placement import get_db_connection


def get_db_for_order():
    conn = get_db_connection()
    order_list = conn.execute("""SELECT *
                    FROM soldiers
                    ORDER BY distance DESC
                    """).fetchall()
    received = []
    on_hold = []
    received += order_list[0 : 160]
    on_hold += order_list[160: ]

    return received , on_hold


