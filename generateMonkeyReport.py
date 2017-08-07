import os
from base import  Template as MicroTemplate

template_dir = os.path.join(os.getcwd(), 'templates')
# template_dir = r"E:\my_work\auto\resultParser\templates"
template_file = "report_template_monkey.html"
def generateReport(resultStr, output):
    template_content = read_html(template_dir, template_file)
    rendered = MicroTemplate(template_content).render(**resultStr)

    resultPath = os.path.join(output)
    if not os.path.exists(os.path.join(os.getcwd(), "reports")):
        os.mkdir(os.path.join(os.getcwd(), "reports"))
    file(resultPath, 'w').write(rendered)

def read_html(p_template_dir,p_template_file):
    html_file_path = os.path.join(p_template_dir, "%s" % p_template_file)
    with open(html_file_path) as html_file:
        html = html_file.read()
    return html

if __name__ == "__main__":
    str1 = {"pkgName": "com.kingsoft.email",
            "duration": "3",
            "crashCount": '2',
            "anrCount": "3",
            "deviceInfo": "nokia",
            "tasks": [{"logPath": "dwdw",
                       "crashCount": "2",
                       "anrCount": "1" },
                      {"logPath": "dwdwdf",
                       "crashCount": "1",
                       "anrCount": "2"}]}
    generateReport(str1, "adb.html")