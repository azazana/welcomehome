from unittest.mock import patch

from mysqlx import OperationalError as MysqlError
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTest(SimpleTestCase):
    """Test commands."""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if database is not ready."""
        patched_check.return_value = True
        call_command('wait_for_db')
        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting OperationError."""
        patched_check.side_effect = [MysqlError] * 2 + [OperationalError] * 3
        +[True]

        call_command('wait_for_db')
        self.assertEqual(patched_check.call_count, 6)

        patched_check.assert_called_once_with(databases=['default'])
