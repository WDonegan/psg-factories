import re

input_str: str = '''

'''

output_text = '''import PySimpleGUI as sg
from .base import GeneratorBase


class _TYPE_(GeneratorBase):
_STRINGS_
    def reset_params(self):
        self.__parameters__ = {
_PARAMS_        }

    def make(self, key: str, param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        active_params: dict = self.__get_params__(param_key)
        return sg._TYPE_(**active_params)
'''

input_list: list = input_str.split('\n')

pattern: re.Pattern = re.compile(r'\w+')
match = pattern.match(input_list[1])
input_list[0] = match[0]
input_list[1] = input_list[1][match.span(0)[1]+1:]

for i in range(2, len(input_list)):
    input_list[i] = input_list[i].strip()

strings: str = ''
for ln in input_list:
    if ln == input_list[0]:
        continue
    match = pattern.match(ln)
    if not match:
        continue
    param_name: str = pattern.match(ln)[0]
    if len(param_name) <= 1:
        continue
    strings += f"    {param_name.upper()} = '{param_name}'\n"

params: str = ''
for ln in input_list:
    if ln == input_list[0]:
        continue
    match = pattern.match(ln)
    if not match:
        continue
    param_name: str = pattern.match(ln)[0]
    if len(param_name) <= 1:
        continue
    params += f"            self.{param_name.upper()}: (False, None),\n"

output_text = output_text.replace('_TYPE_', input_list[0])
output_text = output_text.replace('_STRINGS_', strings)
output_text = output_text.replace('_PARAMS_', params)

print(output_text)

with open(f'src/SgFactory/{input_list[0].lower()}.py', 'w') as file:
    file.write(output_text)
