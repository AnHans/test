# Software-Development-Life-Cycle am Beispiel

Dieses kleine Projekt demonstriert ein Software-Development-Life-Cycle am Beispiel eines Statistik-Moduls. Für beliebige Werte sollen statistische Kennzahlen ermittelt werden, wie z.B. Maximum, Minimum und arithmetisches Mittel. Für die Ermittlung des minimalen Wertes liegt eine Funktion und zugehörige Unit-Tests vor.
Damit ihr ein Gefühl bekommt, wohin die Reise geht, schaut euch gerne zunächst mal das Modul [Automatisierte Pipeline im Software Developement Lifecycle (SDLC)](https://moodle.itech-bs14.de/course/view.php?id=570) und dort die Präsentation zum Einstieg in den SDLC.
Um eine eigene kleine Pipeline zu erstellen, sind folgende Schritte notwendig:
1.  Entwicklung und Erstellung des Quellcodes und der Unit Tests
2.  Testen und Quellcode verbessern, dabei Versionsverwaltungstool z.B. Git einsetzen
3.  Anwendung einer Continues-Delivery-Pipeline mit GitLab

## Unit Tests
Das Modul *test_maximum.py* zeigt einen Unit Test für das Modul *maximum.py* für unterschiedliche Testfälle. Grundsätzlich kann ein Testfall drei verschiedene Ergebnisse haben:
*  Er kann gelingen (success) -> Ergebnis und Erwartung stimmen überein
*  Er kann fehlschlagen (failure) -> Ergebnis und Erwartung stimmen nicht überein
*  Er kann eine Ausnahme erzeugen (error) -> Test ist mit einem internen Fehler abgebrochen, dies deutet auf fehlerhaften Testcode hin.

Informationen und Übungen zu Unit Tests enthält das Moodle Modul "[Automatisiertes Testen mit Unit- und Integrationstest](https://moodle.itech-bs14.de/course/view.php?id=464)" an.

## Versionsverwaltungstool Git einsetzen
Link:  
[git- Der einfache Einstieg](https://rogerdudler.github.io/git-guide/index.de.html)   - zum Einstieg sehr zu empfehlen  
[git cheat sheet](https://rogerdudler.github.io/git-guide/files/git_cheat_sheet.pdf)

Ein paar Tipps zum schnellen Einstieg:
* Git installieren, in Windows die Konsolanwendung Git Bash nutzen
* Dateiverzeichnis auf dem eigenen Rechner für das Repository anlegen -> lokales Repository
* Git Bash starten und in das angelegte Dateverzeichnis wechseln (mit dem LINUX Kommando _cd_, denn Git Bash versteht Linux )
* lokales Repository einrichten mit dem Befehl: _git init_
* Arbeitskopie eines vorhandenen Repositorys z.B. bei Gitlab erstellen mit dem Befehl _git clone_ oder
* neu erstellte oder geänderte Dateien mit _git add_ und _git commit_ in das lokale Repository aufnehmen 
* Änderungen an das entfernte Repository hochladen mit _git push_
* mit _git status_ Überblick verschaffen

## GitLab-Projekt (Repository) aufsetzen
* Account für [GitLab anlegen](https://gitlab.com/)
* SSH Schlüssel generieren:
    * Hinweise zur [Schlüsselgenerierung aus GitLab](https://gitlab.com/help/ssh/README#generating-a-new-ssh-key-pair)
    * Git-Bash starten
        * Schlüssel generieren mit dem Befehl  ```ssh-keygen -t rsa```
    * Schlüssel im GitLab-Account unter Settings/SSH Keys speichern
        * Achtung: ggf. unterschiedliche Schüssel für Schulrechner und privaten Rechner generieren bzw. notwendig
* [Projekt in Gitlab erstellen](https://docs.gitlab.com/ee/gitlab-basics/create-project.html)
* Übertragung mit SSH funktioniert in der Schule nicht!

## CI/CD Pipeline mit GitLab einrichten
Was ist das Ziel?
*  die geschriebenen Tests sollen automatisch nach einem _push_ ausgeführt werden,
*  außerdem möchten wir die Qualität unseres Python-Codes mit [Pylint](https://www.pylint.org/) prüfen und darauf hingewiesen werden, falls wir uns vom [PEP-8-Styleguide](https://www.python.org/dev/peps/pep-0008/#introduction) entfernt haben
*  wenn die vorangegangenen Phasen erfolgreich waren, soll das Python-Programm ausgführt werden

Die Basis für CI/CD in GitLab ist die Datei ```.gitlab-ci.yml```, die auf höchster Ebene des Repositorys angelegt wird. Die Datei beschreibt die Schritte, die der CI/CD-Workflow durchlaufen soll, welche Skripte auzuführen sind und welche Abhängigkeiten es gibt und andere Konfigurationsdetails. Diese Datei wird von GitLab automatisch gefunden und der GitLabRunner führt das darin enthaltene bei jedem push automatisch aus. Angezeigt wird die Ausführung auf der GitLab-Seite *CI/CD->Pipelines*.  Der Runner ist eine Art Terminal, der bei der Ausführung auch anzeigt, was er gerade mit welchem Ergebnis tut. Im Falle eines Fehlers erthalten wir ebenfalls eine E-Mail mit der entsprechenden Fehlermeldung.
Das Konfigurieren einer CI/CD-Pipeline in der ```.gitlab-ci.yml```*-Datei erfolgt in [YAML](https://www.codeproject.com/Articles/1214409/Learn-YAML-in-five-minutes) -Syntax. Für die Ausführung des Beispiels wird eine „Docker“-Umgebung verwendet:
```image: python:latest```     
Für das Beispiel wurden 3 Stages definiert:
```  stages:
 - check
 - test
 - run
 ```
Als nächstes werden die auszuführenden Jobs definiert. Zum Beispiel:
```
quality_checker:
  stage: check
  before_script:
   - pip install pylint #install  pylint  (source-code, bug and quality checker)
  script:
    - pylint statistik.py #check source code statistik.py
```
Das bedeutet, der Job *quality_checker* bezieht sich auf die Phase *stage: check* und mit "before_script" können Voraussetzungen festgelegt werden. Die eingetragenen Kommandos werden vom Runner vor der Ausführung eines jeden Jobs zuerst bearbeitet. Es wird also zunächst pylint installiert, und anschließend die Kommandos die unter "script:" stehen ausgeführt.

**Quellen:**   
[Introduction to CI/CD with GitLab](https://docs.gitlab.com/ee/ci/introduction/)   
[GitLab CI/CD Pipeline Configuration Reference](https://docs.gitlab.com/ee/ci/yaml/)    
[Gitlab einrichten](https://machine-learning-blog.de/2019/10/10/continuous-integration-tutorial-gitlab-cicd-einrichten/)   
[Code-Qualität verbessern mit pylint](https://machine-learning-blog.de/2019/10/10/code-qualitat-in-python-pylint-als-linter-fur-python-code-einsetzen/#more-627)
