import falcon


def test_headers(client):
    resp = client.simulate_get('/first')
    assert resp.headers['content-type'] == falcon.MEDIA_HTML
    assert resp.status == falcon.HTTP_200
    assert resp.status_code == 200


def test_html_p_tag(client, soup, jinja_context):
    resp = client.simulate_get('/first')
    soup = soup(resp.text)
    assert soup.find('p').text == jinja_context['quote']


def test_html_li_tags(client, soup, jinja_array_context):
    resp = client.simulate_get('/second')
    html = soup(resp.text)
    result = [li.text for li in html.find_all('li')]
    assert result == jinja_array_context['frameworks']
