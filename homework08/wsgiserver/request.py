import dataclasses
import typing as tp
import urllib.parse

from httpserver import HTTPRequest


@dataclasses.dataclass
class WSGIRequest(HTTPRequest):
    def to_environ(self) -> tp.Dict[str, tp.Any]:
        environ = {
            "REQUEST_METHOD": self.method,
            "SCRIPT_NAME": "",
            "CONTENT_TYPE": self.headers.get("content-type", ""),
            "CONTENT_LENGTH": len(self.body),
        }
        if "?" in self.url:
            path, query = self.url.split("?", 1)
        else:
            path, query = self.url, ""

        environ["PATH_INFO"] = urllib.parse.unquote(path, "iso-8859-1")
        environ["QUERY_STRING"] = query
        return environ
