# -*- coding: utf-8 -*-
"""

SQLpie License (MIT License)
Copyright (c) 2011-2016 André Lessa, http://sqlpie.com
See LICENSE file.

"""

import json
import sqlpie

class ServiceSummarizationTests(object):
    #
    # Service Summarization Tests
    #

    def run_before_service_summarization_tests(self):
        response = self.app.post('/document/reset', data=json.dumps({}), content_type = 'application/json')

        resume_file = open('tests/_support_files/resume_java001.txt')
        document01 = resume_file.read()

        resume_file = open('tests/_support_files/news001.txt')
        document02 = resume_file.read()

        resume_file = open('tests/_support_files/news002.txt')
        document03 = resume_file.read()

        resume_file = open('tests/_support_files/news003.txt')
        document04 = resume_file.read()

        documents = {"documents":[{"_id":"001", "_bucket":"resumes", "resume":document01},{"_id":"002", "_bucket":"news", "article":document02},{"_id":"003", "_bucket":"news", "article":document03},{"_id":"004", "_bucket":"news", "article":document04}]}
        response = self.app.post('/document/put', data=json.dumps(documents), content_type = 'application/json')

    def test_service_summarization_01_single_document_max_sentences(self):
        self.run_before_service_summarization_tests()

        request = {"documents":[{"title":"Google To Launch An Artificial Intelligence Messenger Service To Rival Facebook M: Reports","summary":"According to sources close to the Wall Street Journal, Google is looking into launching a new mobile based messenger service underpinned by artificial intelligence. “For its new service, Google, a unit of Alphabet Inc., plans to integrate chatbots, software programs that answer questions inside a messaging app,” the article claims. Further sources have indicated that Nick Fox, currently vice president of communications at Google, has been leading a team for over a year to develop this new service."},{"title":"Google’s new messaging app to have artificial intelligence","summary":"Google is going to give a twist to normal messaging apps by coming up with a new one that employs artificial intelligence. The technology will bring Google’s data smarts to a chat bot service in the software. The new chat service will be an interesting feature allowing users to talk with friends or ask question of the chat bot. In return, the chat bot will look for answers from the search engine giant’s vast map of the internet."}], "options":{"max_sentences":1}}
        response = self.app.post('/service/summarization', data=json.dumps(request), content_type = 'application/json')
        json_response = json.loads(response.data)
        assert json_response["success"] == True
        assert json_response["results"] == {u'fields': {u'title': [[u'Google To Launch An Artificial Intelligence Messenger Service To Rival Facebook M: Reports', 54.0]], u'summary': [[u'For its new service, Google, a unit of Alphabet Inc., plans to integrate chatbots, software programs that answer questions inside a messaging app," the article claims. Further sources have indicated that Nick Fox, currently vice president of communications at Google, has been leading a team for over a year to develop this new service.', 115.45085]]}, u'field_entities': {u'title': [u'Reports', u'Google'], u'summary': [u'Google', u'Wall Street Journal', u'Nick Fox', u'Alphabet Inc']}, u'field_keywords': {u'title': [u'artificial intelligence', u'google', u'reports', u'service', u'launch'], u'summary': [u'chat bot', u'google', u'service', u'artificial intelligence', u'sources']}}, "Actual Response : %r" % json_response

    def test_service_summarization_02_single_document_max_summary_size(self):
        self.run_before_service_summarization_tests()

        request = {"documents":[{"title":"Google To Launch An Artificial Intelligence Messenger Service To Rival Facebook M: Reports","summary":"According to sources close to the Wall Street Journal, Google is looking into launching a new mobile based messenger service underpinned by artificial intelligence. “For its new service, Google, a unit of Alphabet Inc., plans to integrate chatbots, software programs that answer questions inside a messaging app,” the article claims. Further sources have indicated that Nick Fox, currently vice president of communications at Google, has been leading a team for over a year to develop this new service."},{"title":"Google’s new messaging app to have artificial intelligence","summary":"Google is going to give a twist to normal messaging apps by coming up with a new one that employs artificial intelligence. The technology will bring Google’s data smarts to a chat bot service in the software. The new chat service will be an interesting feature allowing users to talk with friends or ask question of the chat bot. In return, the chat bot will look for answers from the search engine giant’s vast map of the internet."}], "options":{"max_summary_size":512}}
        response = self.app.post('/service/summarization', data=json.dumps(request), content_type = 'application/json')
        json_response = json.loads(response.data)
        assert json_response["success"] == True
        assert json_response["results"] == {u'fields': {u'title': [[u'Google To Launch An Artificial Intelligence Messenger Service To Rival Facebook M: Reports', 54.0]], u'summary': [[u'According to sources close to the Wall Street Journal, Google is looking into launching a new mobile based messenger service underpinned by artificial intelligence.', 100.0], [u'For its new service, Google, a unit of Alphabet Inc., plans to integrate chatbots, software programs that answer questions inside a messaging app," the article claims. Further sources have indicated that Nick Fox, currently vice president of communications at Google, has been leading a team for over a year to develop this new service.', 115.45085]]}, u'field_entities': {u'title': [u'Reports', u'Google'], u'summary': [u'Google', u'Wall Street Journal', u'Nick Fox', u'Alphabet Inc']}, u'field_keywords': {u'title': [u'artificial intelligence', u'google', u'reports', u'service', u'launch'], u'summary': [u'chat bot', u'google', u'service', u'artificial intelligence', u'sources']}}, "Actual Response : %r" % json_response

    def test_service_summarization_03_single_document_max_summary_percent(self):
        self.run_before_service_summarization_tests()

        request = {"documents":[{"title":"Google To Launch An Artificial Intelligence Messenger Service To Rival Facebook M: Reports","summary":"According to sources close to the Wall Street Journal, Google is looking into launching a new mobile based messenger service underpinned by artificial intelligence. “For its new service, Google, a unit of Alphabet Inc., plans to integrate chatbots, software programs that answer questions inside a messaging app,” the article claims. Further sources have indicated that Nick Fox, currently vice president of communications at Google, has been leading a team for over a year to develop this new service."},{"title":"Google’s new messaging app to have artificial intelligence","summary":"Google is going to give a twist to normal messaging apps by coming up with a new one that employs artificial intelligence. The technology will bring Google’s data smarts to a chat bot service in the software. The new chat service will be an interesting feature allowing users to talk with friends or ask question of the chat bot. In return, the chat bot will look for answers from the search engine giant’s vast map of the internet."}], "options":{"max_summary_percent":50}}
        response = self.app.post('/service/summarization', data=json.dumps(request), content_type = 'application/json')
        json_response = json.loads(response.data)
        assert json_response["success"] == True
        assert json_response["results"] == {u'fields': {u'title': [[u'Google To Launch An Artificial Intelligence Messenger Service To Rival Facebook M: Reports', 54.0]], u'summary': [[u'According to sources close to the Wall Street Journal, Google is looking into launching a new mobile based messenger service underpinned by artificial intelligence.', 100.0], [u'For its new service, Google, a unit of Alphabet Inc., plans to integrate chatbots, software programs that answer questions inside a messaging app," the article claims. Further sources have indicated that Nick Fox, currently vice president of communications at Google, has been leading a team for over a year to develop this new service.', 115.45085], [u'The new chat service will be an interesting feature allowing users to talk with friends or ask question of the chat bot.', 73.888544], [u"In return, the chat bot will look for answers from the search engine giant's vast map of the internet.", 64.0]]}, u'field_entities': {u'title': [u'Reports', u'Google'], u'summary': [u'Google', u'Wall Street Journal', u'Nick Fox', u'Alphabet Inc']}, u'field_keywords': {u'title': [u'artificial intelligence', u'google', u'reports', u'service', u'launch'], u'summary': [u'chat bot', u'google', u'service', u'artificial intelligence', u'sources']}}, "Actual Response : %r" % json_response

    def test_service_summarization_04_single_document_fields_to_summarize_and_max_summary_percent(self):
        self.run_before_service_summarization_tests()

        request = {"documents":[{"title":"Google To Launch An Artificial Intelligence Messenger Service To Rival Facebook M: Reports","summary":"According to sources close to the Wall Street Journal, Google is looking into launching a new mobile based messenger service underpinned by artificial intelligence. “For its new service, Google, a unit of Alphabet Inc., plans to integrate chatbots, software programs that answer questions inside a messaging app,” the article claims. Further sources have indicated that Nick Fox, currently vice president of communications at Google, has been leading a team for over a year to develop this new service."},{"title":"Google’s new messaging app to have artificial intelligence","summary":"Google is going to give a twist to normal messaging apps by coming up with a new one that employs artificial intelligence. The technology will bring Google’s data smarts to a chat bot service in the software. The new chat service will be an interesting feature allowing users to talk with friends or ask question of the chat bot. In return, the chat bot will look for answers from the search engine giant’s vast map of the internet."}], "options":{"max_summary_percent":50, "fields_to_summarize":["title"]}}
        response = self.app.post('/service/summarization', data=json.dumps(request), content_type = 'application/json')
        json_response = json.loads(response.data)
        assert json_response["success"] == True
        assert json_response["results"] == {'fields': {'title': [['Google To Launch An Artificial Intelligence Messenger Service To Rival Facebook M: Reports', 54.0]]}, 'field_entities': {'title': ['Reports', 'Google']}, 'field_keywords': {'title': ['artificial intelligence', 'google', 'reports', 'service', 'launch']}}, "Actual Response : %r" % json_response

    def test_service_summarization_05_single_document_from_database(self):
        self.run_before_service_summarization_tests()

        request = {"bucket":"resumes", "documents":["001"], "options":{"max_keywords":10, "max_entities":5, "fields_to_summarize":["resume"]}}
        response = self.app.post('/service/summarization', data=json.dumps(request), content_type = 'application/json')
        json_response = json.loads(response.data)
        assert json_response["success"] == True
        assert json_response["results"] == {u'fields': {u'resume': [[u'Java/J2EE Developer : Royals Bank - Pittsburgh, PA : September 2012 to Present', 95.323382], [u'well experienced in working with Java Server Faces(JSF)', 81.656873], [u'worked extensively with Struts 2 framework coding the Action Support class, the Service layer, the data access layer, domain models.', 163.271644], [u'implemented Spring 3.1 framework for flexible dependency injection and annotation-based configuration styles.', 94.310422], [u'Web Sphere Application server 8.0 was used to make the data source configuration to connect the application to the required database to retrieve or update necessary information.', 104.795324], [u'Development Tools: Java 1.6, JSF, Richfaces, Spring, Soap and RestFul Web Services, SOAP UI Pro, EXTJS, XML, JSON, Javascript, HTML 4.01, Apache Axis 2.1, MySql, Junit4.', 211.457587], [u'performed extensive use of Servlets & JSP for presentation layer along with Javascript for the client side validations.', 87.907295], [u'in-depth knowledge/experience of Web 2.0, Javascript, JQuery, EXTJS, W3C Standards', 93.538486], [u'designed the application based on Spring framework.', 76.005765], [u'Technical Environment: J2EE, Servlets, JSP, Java 1.6, EXTJS, Spring 3.0 , SpringSource Tool Suite 2.8.0, JBoss, HTML 4.01, SQL, CSS, Javascript, SDLC, UML, Maven.', 305.459387]]}, u'field_entities': {u'resume': [u'Java', u'Javascript', u'Spring', u'Servlets', u'Worked', u'Web Sphere Application', u'Web', u'W3C Standards', u'User Interface', u'Technical Environment']}, u'field_keywords': {u'resume': [u'java 1', u'web services', u'spring 3', u'worked', u'presentation layer']}}, "Actual Response : %r" % json_response

    def test_service_summarization_06_invalid_multiple_documents_from_database(self):
        self.run_before_service_summarization_tests()

        request = {"bucket":"news", "documents":["002", "003"], "options":{"max_keywords":10, "max_entities":5, "fields_to_summarize":["news"]}}
        response = self.app.post('/service/summarization', data=json.dumps(request), content_type = 'application/json')
        json_response = json.loads(response.data)
        assert json_response["success"] == True
        assert json_response["results"] == {'fields': {}, 'field_entities': {}, 'field_keywords': {}}, "Actual Response : %r" % json_response

    def test_service_summarization_07_multiple_documents_from_database(self):
        self.run_before_service_summarization_tests()

        request = {"bucket":"news", "documents":["002", "003"], "options":{"max_keywords":10, "max_entities":5, "fields_to_summarize":["article"]}}
        response = self.app.post('/service/summarization', data=json.dumps(request), content_type = 'application/json')
        json_response = json.loads(response.data)
        assert json_response["success"] == True
        assert json_response["results"] == {u'fields': {u'article': [[u'Google To Launch An Artificial Intelligence Messenger Service To Rival Facebook M', 105.0], [u'According to sources close to the Wall Street Journal, Google is looking into launching a new mobile based messenger service underpinned by artificial intelligence.', 117.488434], [u'For its new service, Google, a unit of Alphabet Inc., plans to integrate chatbots, software programs that answer questions inside a messaging app," the article claims.', 76.8], [u"The technology will bring Google's data smarts to a chat bot service in the software.", 37.235325], [u'The new chat service will be an interesting feature allowing users to talk with friends or ask question of the chat bot.', 57.6], [u"In return, the chat bot will look for answers from the search engine giant's vast map of the internet.", 51.97645]]}, u'field_entities': {u'article': [u'Google', u'Wall Street Journal', u'Alphabet Inc']}, u'field_keywords': {u'article': [u'artificial intelligence', u'google', u'messenger service', u'chat bot', u'messaging app']}}, "Actual Response : %r" % json_response

    def test_service_summarization_08_several_documents_from_database(self):
        self.run_before_service_summarization_tests()

        request = {"bucket":"news", "documents":["002", "003", "004"], "options":{"max_keywords":10, "max_entities":5, "fields_to_summarize":["article"]}}
        response = self.app.post('/service/summarization', data=json.dumps(request), content_type = 'application/json')
        json_response = json.loads(response.data)
        assert json_response["success"] == True
        assert json_response["results"] == {u'fields': {u'article': [[u'Google To Launch An Artificial Intelligence Messenger Service To Rival Facebook M', 113.666667], [u'According to sources close to the Wall Street Journal, Google is looking into launching a new mobile based messenger service underpinned by artificial intelligence.', 184.402963], [u'For its new service, Google, a unit of Alphabet Inc., plans to integrate chatbots, software programs that answer questions inside a messaging app," the article claims.', 94.191421], [u"Google's new messaging app to have artificial intelligence", 55.0], [u"In return, the chat bot will look for answers from the search engine giant's vast map of the internet.", 43.472964], [u'Google reportedly working on an artificially intelligent messaging app', 104.495012], [u'Google may be working on a new messaging app that would use artificial intelligence to give users answers to search queries, according to a report by The Wall Street Journal.', 250.0]]}, u'field_entities': {u'article': [u'Google', u'Wall Street Journal', u'The Wall Street Journal', u'Alphabet Inc']}, u'field_keywords': {u'article': [u'artificial intelligence', u'google', u'messaging app', u'messenger service', u'chat bot']}}, "Actual Response : %r" % json_response

    def test_service_summarization_09_single_snippet(self):
        request = {"documents":[{"title":"Google To Launch An Artificial Intelligence Messenger Service To Rival ...", "snippet":"According to sources close to the Wall Street Journal, Google is looking into launching a new mobile based messenger service underpinned by artificial intelligence. “For its new service, Google, a unit of Alphabet Inc., plans to integrate chatbots ..."}], "options":{"max_keywords":100, "fields_to_summarize":["title","snippet"]}}
        response = self.app.post('/service/summarization', data=json.dumps(request), content_type = 'application/json')
        json_response = json.loads(response.data)
        assert json_response["success"] == True
        assert json_response["results"] == {'fields': {'snippet': [['According to sources close to the Wall Street Journal, Google is looking into launching a new mobile based messenger service underpinned by artificial intelligence.', 48.0]], 'title': [['Google To Launch An Artificial Intelligence Messenger Service To Rival ...', 7.0]]}, 'field_entities': {'snippet': ['Google', 'Wall Street Journal', 'Alphabet Inc'], 'title': []}, 'field_keywords': {'snippet': ['google', 'service', 'wall street journal', 'alphabet inc', 'based'], 'title': ['google', 'service', 'launch', 'intelligence', 'artificial']}}, "Actual Response : %r" % json_response

    def test_service_summarization_10_multiple_snippets(self):
        request = {"documents":[{"title":"Google To Launch An Artificial Intelligence Messenger Service To Rival ...", "snippet":"According to sources close to the Wall Street Journal, Google is looking into launching a new mobile based messenger service underpinned by artificial intelligence. According to sources close to the Wall Street Journal, Google is looking into launching a new mobile based messenger service underpinned by artificial intelligence. “For its new service, Google, a unit of Alphabet Inc., plans to integrate chatbots ..."},{"title":"Google plots WhatsApp rival with artificial intelligence features", "snippet":"Google is building a new mobile-messaging service that taps its artificial intelligence know-how and so-called chatbot technology to try to catch rivals including Facebook Inc. in the fast-growing arena, according to people familiar with the matter ..."},{"title":"Google working on an Artificial Intelligence-based chat app: report", "snippet":"The new service would tap into Google's artificial intelligence know-how, integrating chatbots, or software programs that answer questions, inside a messaging app, the Journal reported on Tuesday, citing people familiar with the matter. MUST READ: ..."},{"title":"Google's New Messaging App with Artificial Intelligence: WSJ", "snippet":"Yes, the new service will leverage Google's artificial intelligence know-how, combining chatbots. These are software programs within a messaging app that search the Internet to answer a question. The new app will let users send texts or a chatbot ..."},{"title":"Google's new messaging app may feature artificial intelligence", "snippet":"When Facebook's “M” hits Messenger in the coming months, it might arrive with some major competition. According to The Wall Street Journal, Google is building an intelligent messaging service of its own that will utilize chatbot technology, making the ..."},{"title":"Google Reportedly Launching Artificial Intelligence Messaging Service", "snippet":"The platform would integrate chatbots, software designed to answer questions using artificial intelligence, to help bring an enhanced search experience with Google. google The sources said that Google could even open source the chatbots, allowing ..."},{"title":"Google developing new messaging app, may feature artificial intelligence",  "snippet":"Bengaluru:Google, part of Alphabet Inc, is building a new mobile messaging application to better compete with rival services such as those offered by Facebook Inc, the Wall Street Journal reported. The new service would tap into Google's artificial ..."},{"title":"Google working on artificial intelligence messaging app", "snippet":"The company is working on a new messaging app that uses artificial intelligence to provide users with answers to search queries, according to a new report. Details on exactly how the messaging service would work are slim but chatbots could play a ..."},{ "title":"Google's new messaging app to have artificial intelligence", "snippet":"Google is going to give a twist to normal messaging apps by coming up with a new one that employs artificial intelligence. The technology will bring Google's data smarts to a chat bot service in the software. The new chat service will be an interesting ..."},{"title":"Google tries to play catch-up with smarter messenger with built-in artificial ...", "snippet":"Google is coming up with a smarter messenger or a chat platform with built-in artificial intelligence to play catch-up with rivals like Skype, WhatsApp, Facebook Messenger and Viber. The Mountain View-based internet giant first played its hand at the ..."},{"title":"Google may be working on messaging app infused with artificial intelligence", "snippet":"Google is working on a new messaging app that will employ artificial intelligence to bring some of the company's data smarts to a chat bot service in the software, according to a report in The Wall Street Journal. The new chat service would allow users ..."},{"title":"Google developing AI-based messaging service: Report", "snippet":"A couple of news items from Google today: First, the company is reportedly working on a new kind of artificial intelligence-based messaging service, in an attempt to compete with Facebook's WhatsApp and Messenger, according to the Wall Street Journal."},{"title":"Google is working on an artificially intelligent messaging app, report says", "snippet":"Google is far from the first tech company to integrate artificial intelligence into a messaging product. Facebook is also working on an A.I.-based assistant, called \"M,\" which is part of the company's Messenger app. Though M relies on a combination of ..."}], "options":{"max_keywords":100, "fields_to_summarize":["title","snippet"]}}
        response = self.app.post('/service/summarization', data=json.dumps(request), content_type = 'application/json')
        json_response = json.loads(response.data)
        assert json_response["success"] == True
        assert json_response["results"] == {u'fields': {u'snippet': [[u'According to sources close to the Wall Street Journal, Google is looking into launching a new mobile based messenger service underpinned by artificial intelligence.', 463.272727]], u'title': [[u'Google To Launch An Artificial Intelligence Messenger Service To Rival ...', 146.25], [u'Google plots WhatsApp rival with artificial intelligence features', 133.509017], [u'Google working on an Artificial Intelligence-based chat app: report', 160.416667], [u"Google's New Messaging App with Artificial Intelligence: WSJ", 126.0], [u"Google's new messaging app may feature artificial intelligence", 119.0], [u'Google working on artificial intelligence messaging app', 96.954828], [u"Google's new messaging app to have artificial intelligence", 92.75], [u'Google may be working on messaging app infused with artificial intelligence', 169.166667], [u'Google developing AI-based messaging service: Report', 113.685674], [u'Google is working on an artificially intelligent messaging app, report says', 198.25]]}, u'field_entities': {u'snippet': [u'Google', u'Wall Street Journal', u'Messenger', u'WhatsApp', u'The Wall Street Journal', u'Facebook Inc', u'Facebook', u'Alphabet Inc', u'When Facebook', u'Viber'], u'title': [u'Google', u'Artificial Intelligence', u'WhatsApp', u'Report', u'New Messaging App']}, u'field_keywords': {u'snippet': [u'messaging service', u'artificial intelligence', u'google', u'wall street', u'journal reported'], u'title': [u'artificial intelligence', u'messaging app', u'google working', u'report', u'service']}}, "Actual Response : %r" % json_response