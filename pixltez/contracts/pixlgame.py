import smartpy as sp
FA2 = sp.io.import_script_from_url("https://smartpy.io/templates/fa2_lib.py")

class Constants:
    ADMINISTRATOR = "tz1hmPbNNcaH91bkrYDeyAbUmYzjbPtJjPQR"

class PiXLGame(FA2.Fa2Nft):
    @sp.entry_point
    def mint(self, batch):
        with sp.for_("action", batch) as action:
            token_id = sp.compute(self.data.last_token_id)
            metadata = sp.record(token_id=token_id, token_info=action.metadata)
            self.data.token_metadata[token_id] = metadata
            self.data.ledger[token_id] = action.to_
            self.data.last_token_id += 1


admin = sp.address(Constants.ADMINISTRATOR)
sp.add_compilation_target(
    "PiXLGame", 
    PiXLGame(
        metadata=sp.utils.metadata_of_url("ipfs://example"),
        policy=FA2.OwnerTransfer(),
    )
)
