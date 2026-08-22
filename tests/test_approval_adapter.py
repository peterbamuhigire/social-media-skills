import json
import unittest
from pathlib import Path


class ApprovalAdapterTests(unittest.TestCase):
    def test_adapter_declares_human_gate_for_outbound_actions(self):
        payload = json.loads((Path(__file__).parents[1] / "docs" / "approval-adapter.json").read_text(encoding="utf-8"))
        self.assertEqual(payload["engine"], "social-media")
        actions = {item["action_type"]: item for item in payload["actions"]}
        for action_type in ("social.content.publish", "social.message.send", "social.paid-spend.change"):
            self.assertEqual(actions[action_type]["class"], "L3")
            self.assertTrue(actions[action_type]["preview_required"])
            self.assertTrue(actions[action_type]["idempotency_required"])


if __name__ == "__main__":
    unittest.main()
