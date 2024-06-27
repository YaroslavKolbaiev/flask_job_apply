from flask import Flask, Response, request, abort
from flask_bootstrap import Bootstrap
import os
from threading import Thread

from managers.driver_manager import DriverManager
from managers.rabota_ua_login_manager import RabotaUaLoginManager
from managers.rabota_ua_vacancy_manager import RabotaUaVacancyManager
from managers.dou_login_manager import DouLoginManager
from managers.dou_vacancy_manager import DouVacancyManager

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
Bootstrap(app)


def background_task():
    driver = DriverManager().driver

    print("Logging in to Rabota.ua")
    rabota_ua_login_manager = RabotaUaLoginManager(driver=driver)
    rabota_ua_login_manager.login()

    javascript_vacancies_rabota_ua = RabotaUaVacancyManager(
        driver=driver, category="javascript"
    )
    javascript_vacancies_rabota_ua.vacancy_manager()

    python_vacancies = RabotaUaVacancyManager(driver=driver, category="python")
    python_vacancies.vacancy_manager()

    print("Logging in to Dou.ua")
    dou_login_manager = DouLoginManager(driver=driver)
    dou_login_manager.login()

    front_end_vacancies = DouVacancyManager(driver=driver, category="Front End")
    front_end_vacancies.vacancy_manager()

    back_end_vacancies = DouVacancyManager(driver=driver, category="Node.js")
    back_end_vacancies.vacancy_manager()

    pyhon_dou_vacancies = DouVacancyManager(driver=driver, category="Python")
    pyhon_dou_vacancies.vacancy_manager()

    driver.quit()


@app.route("/")
def run_job_application():
    allowed_host = os.environ.get("ALLOWED_HOST")

    if request.host_url != allowed_host:
        abort(401)

    # Start the background task without waiting for it to complete
    thread = Thread(target=background_task)
    thread.start()

    # Return a response immediately without waiting for the background task
    return Response("Started a background task.", status=200)
