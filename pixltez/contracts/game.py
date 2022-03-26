import smartpy as sp
fa2 = sp.io.import_script_from_url("file:./contracts/fa2.py")

class Constants:
    ADMINISTRATOR = "tz1hmPbNNcaH91bkrYDeyAbUmYzjbPtJjPQR"

class Token(fa2.FA2):
    pass

admin = sp.address(Constants.ADMINISTRATOR)
sp.add_compilation_target("PiXLGame", Token(
    config = fa2.FA2_config(
        single_asset = True,
        non_fungible = False,
        assume_consecutive_token_ids = False
    ),
    admin = admin,
    metadata = sp.big_map({
        "": sp.utils.bytes_of_string("tezos-storage:content"),
        "content": sp.utils.bytes_of_string("""{name: "PiXL"}"""),
    })
))