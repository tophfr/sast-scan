import os

from lib.integration import gitlab


def test_context():
    os.environ["CI_MERGE_REQUEST_IID"] = "test"
    os.environ["CI_MERGE_REQUEST_PROJECT_ID"] = "test"
    context = gitlab.GitLab().get_context({"foo": "bar"})
    assert context["foo"] == "bar"


def test_reports_url():
    url = gitlab.GitLab().get_mr_notes_url(
        {"repositoryName": "bar", "revisionId": "123"}
    )
    assert url == "https://gitlab.com/api/v4/projects/test/merge_requests/test/notes"
