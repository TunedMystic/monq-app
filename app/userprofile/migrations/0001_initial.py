# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('websiteUrl', models.URLField(max_length=80, blank=True)),
                ('accountType', models.CharField(max_length=20)),
                ('defaultSnippetLanguage', models.CharField(default=b'text', max_length=20, choices=[(b'abap', b'ABAP'), (b'actionscript', b'ActionScript'), (b'ada', b'ADA'), (b'apache_conf', b'Apache Conf'), (b'asciidoc', b'AsciiDoc'), (b'assembly_x86', b'Assembly x86'), (b'autohotkey', b'AutoHotKey'), (b'batchfile', b'BatchFile'), (b'c9search', b'C9Search'), (b'c_cpp', b'C and C++'), (b'cirru', b'Cirru'), (b'clojure', b'Clojure'), (b'cobol', b'Cobol'), (b'coffee', b'CoffeeScript'), (b'coldfusion', b'ColdFusion'), (b'csharp', b'C#'), (b'css', b'CSS'), (b'curly', b'Curly'), (b'd', b'D'), (b'dart', b'Dart'), (b'diff', b'Diff'), (b'dockerfile', b'Dockerfile'), (b'dot', b'Dot'), (b'dummy', b'Dummy'), (b'dummysyntax', b'DummySyntax'), (b'eiffel', b'Eiffel'), (b'ejs', b'EJS'), (b'elixir', b'Elixir'), (b'elm', b'Elm'), (b'erlang', b'Erlang'), (b'forth', b'Forth'), (b'ftl', b'FreeMarker'), (b'gcode', b'Gcode'), (b'gherkin', b'Gherkin'), (b'gitignore', b'Gitignore'), (b'glsl', b'Glsl'), (b'golang', b'Go'), (b'groovy', b'Groovy'), (b'haml', b'HAML'), (b'handlebars', b'Handlebars'), (b'haskell', b'Haskell'), (b'haxe', b'haXe'), (b'html', b'HTML'), (b'html_ruby', b'HTML (Ruby)'), (b'ini', b'INI'), (b'io', b'Io'), (b'jack', b'Jack'), (b'jade', b'Jade'), (b'java', b'Java'), (b'javascript', b'JavaScript'), (b'json', b'JSON'), (b'jsoniq', b'JSONiq'), (b'jsp', b'JSP'), (b'jsx', b'JSX'), (b'julia', b'Julia'), (b'latex', b'LaTeX'), (b'less', b'LESS'), (b'liquid', b'Liquid'), (b'lisp', b'Lisp'), (b'livescript', b'LiveScript'), (b'logiql', b'LogiQL'), (b'lsl', b'LSL'), (b'lua', b'Lua'), (b'luapage', b'LuaPage'), (b'lucene', b'Lucene'), (b'makefile', b'Makefile'), (b'markdown', b'Markdown'), (b'matlab', b'MATLAB'), (b'mel', b'MEL'), (b'mushcode', b'MUSHCode'), (b'mysql', b'MySQL'), (b'nix', b'Nix'), (b'objectivec', b'Objective-C'), (b'ocaml', b'OCaml'), (b'pascal', b'Pascal'), (b'perl', b'Perl'), (b'pgsql', b'pgSQL'), (b'php', b'PHP'), (b'powershell', b'Powershell'), (b'praat', b'Praat'), (b'prolog', b'Prolog'), (b'properties', b'Properties'), (b'protobuf', b'Protobuf'), (b'python', b'Python'), (b'r', b'R'), (b'rdoc', b'RDoc'), (b'rhtml', b'RHTML'), (b'ruby', b'Ruby'), (b'rust', b'Rust'), (b'sass', b'SASS'), (b'scad', b'SCAD'), (b'scala', b'Scala'), (b'scheme', b'Scheme'), (b'scss', b'SCSS'), (b'sh', b'SH'), (b'sjs', b'SJS'), (b'smarty', b'Smarty'), (b'snippets', b'snippets'), (b'soy_template', b'Soy Template'), (b'space', b'Space'), (b'sql', b'SQL'), (b'stylus', b'Stylus'), (b'svg', b'SVG'), (b'tcl', b'Tcl'), (b'tex', b'Tex'), (b'text', b'Text'), (b'textile', b'Textile'), (b'toml', b'Toml'), (b'twig', b'Twig'), (b'typescript', b'Typescript'), (b'vala', b'Vala'), (b'vbscript', b'VBScript'), (b'velocity', b'Velocity'), (b'verilog', b'Verilog'), (b'vhdl', b'VHDL'), (b'xml', b'XML'), (b'xquery', b'XQuery'), (b'yaml', b'YAML')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
