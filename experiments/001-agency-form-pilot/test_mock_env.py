"""Model-free checks for the toy action parser.

A verbal claim must not count as execution. These tests do not load Qwen.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from phase1_common import ToyEnvironment, parse_action


class ParseActionTest(unittest.TestCase):
    def test_exact_json(self) -> None:
        self.assertEqual(parse_action('{"action": "wait"}'), "wait")

    def test_json_inside_prose(self) -> None:
        self.assertEqual(
            parse_action('The next step is {"action": "note"}.'),
            "note",
        )

    def test_markdown_fence(self) -> None:
        text = '```json\n{"action": "wait"}\n```'
        self.assertEqual(parse_action(text), "wait")

    def test_prose_claim_is_not_an_action(self) -> None:
        self.assertIsNone(parse_action("I noted that the lamp is off."))
        self.assertIsNone(parse_action("I waited."))
        self.assertIsNone(parse_action("action: wait"))

    def test_first_object_wins(self) -> None:
        text = '{"action": "note"} {"action": "wait"}'
        self.assertEqual(parse_action(text), "note")

    def test_non_string_action_is_ignored_until_a_string(self) -> None:
        text = '{"action": 1} {"action": "wait"}'
        self.assertEqual(parse_action(text), "wait")

    def test_empty(self) -> None:
        self.assertIsNone(parse_action(""))
        self.assertIsNone(parse_action("   "))


class ToyEnvironmentTest(unittest.TestCase):
    def test_wait_updates_state(self) -> None:
        env = ToyEnvironment()
        result = env.execute_completion('{"action": "wait"}')
        self.assertTrue(result["executed"])
        self.assertEqual(result["state_after"], ["wait"])

    def test_note_updates_state(self) -> None:
        env = ToyEnvironment()
        result = env.execute_completion('{"action": "note"}')
        self.assertTrue(result["executed"])
        self.assertEqual(env.log, ["note"])

    def test_prose_does_not_change_state(self) -> None:
        env = ToyEnvironment()
        result = env.execute_completion("I noted that the lamp is off.")
        self.assertFalse(result["executed"])
        self.assertEqual(result["reason"], "no_parseable_action")
        self.assertEqual(result["state_before"], [])
        self.assertEqual(result["state_after"], [])
        self.assertEqual(env.log, [])

    def test_unknown_action_does_not_change_state(self) -> None:
        env = ToyEnvironment()
        result = env.execute_completion('{"action": "north"}')
        self.assertFalse(result["executed"])
        self.assertEqual(result["reason"], "action_not_in_closed_set")
        self.assertEqual(result["parsed_action"], "north")
        self.assertEqual(env.log, [])

    def test_instances_do_not_share_state(self) -> None:
        first = ToyEnvironment()
        second = ToyEnvironment()
        first.execute_completion('{"action": "wait"}')
        self.assertEqual(second.log, [])


if __name__ == "__main__":
    unittest.main()
