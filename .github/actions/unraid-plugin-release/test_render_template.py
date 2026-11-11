import json
import os
import tempfile
import unittest
from unittest import mock

from jinja2 import UndefinedError

from render_template import render


class RenderTemplateTest(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.dir.cleanup)

    def write(self, name, text):
        path = os.path.join(self.dir.name, name)
        with open(path, 'w') as file:
            file.write(text)
        return path

    def output(self):
        return os.path.join(self.dir.name, 'out')

    def read_output(self):
        with open(self.output()) as file:
            return file.read()

    def test_data_keys_and_env_are_variables(self):
        template = self.write('t.j2', '{{ name }}={{ env["RENDER_TEST_VALUE"] }}\n')
        data = self.write('d.json', json.dumps({'name': 'x'}))
        with mock.patch.dict(os.environ, {'RENDER_TEST_VALUE': 'v'}):
            render(template, self.output(), data)
        self.assertEqual(self.read_output(), 'x=v\n')

    def test_undefined_renders_empty_by_default(self):
        template = self.write('t.j2', '[{{ missing }}]\n')
        render(template, self.output())
        self.assertEqual(self.read_output(), '[]\n')

    def test_strict_fails_on_undefined(self):
        template = self.write('t.j2', '[{{ missing }}]\n')
        with self.assertRaises(UndefinedError):
            render(template, self.output(), strict=True)


if __name__ == '__main__':
    unittest.main()
