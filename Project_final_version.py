import sys
import io
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QHeaderView, QMessageBox, QComboBox, QTableWidgetItem, QAbstractItemView
from PyQt6.QtGui import QAction, QPixmap
from PyQt6.QtCore import Qt


main_pyqt = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>778</width>
    <height>583</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Главное окно</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="horizontalLayoutWidget_3">
    <property name="geometry">
     <rect>
      <x>68</x>
      <y>10</y>
      <width>671</width>
      <height>91</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout_3">
     <property name="sizeConstraint">
      <enum>QLayout::SetDefaultConstraint</enum>
     </property>
     <property name="topMargin">
      <number>0</number>
     </property>
     <item>
      <widget class="QLineEdit" name="lineEdit">
       <property name="enabled">
        <bool>true</bool>
       </property>
       <property name="text">
        <string/>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QComboBox" name="column_selector"/>
     </item>
     <item>
      <widget class="QPushButton" name="find_button">
       <property name="text">
        <string>найти</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>100</y>
      <width>77</width>
      <height>101</height>
     </rect>
    </property>
    <property name="text">
     <string>В процессе:</string>
    </property>
   </widget>
   <widget class="QTableWidget" name="progress_table">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>130</y>
      <width>481</width>
      <height>261</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="exitbutton">
    <property name="geometry">
     <rect>
      <x>660</x>
      <y>500</y>
      <width>91</width>
      <height>32</height>
     </rect>
    </property>
    <property name="text">
     <string>Выход</string>
    </property>
   </widget>
   <widget class="QPushButton" name="infobutton">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>500</y>
      <width>91</width>
      <height>32</height>
     </rect>
    </property>
    <property name="text">
     <string>info</string>
    </property>
   </widget>
   <widget class="QWidget" name="gridLayoutWidget">
    <property name="geometry">
     <rect>
      <x>610</x>
      <y>220</y>
      <width>147</width>
      <height>80</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout">
     <item row="0" column="0">
      <widget class="QLabel" name="label_3">
       <property name="enabled">
        <bool>true</bool>
       </property>
       <property name="text">
        <string>Ждут оценки:</string>
       </property>
      </widget>
     </item>
     <item row="0" column="1">
      <widget class="QPushButton" name="films_score_button">
       <property name="text">
        <string>7</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

background_pyqt = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>201</width>
    <height>212</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Тема</string>
  </property>
  <widget class="QWidget" name="verticalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>60</x>
     <y>110</y>
     <width>81</width>
     <height>80</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QRadioButton" name="white">
      <property name="text">
       <string>Светлая</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QRadioButton" name="black">
      <property name="text">
       <string>Темная</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>50</x>
     <y>20</y>
     <width>111</width>
     <height>71</height>
    </rect>
   </property>
   <property name="text">
    <string>Выберите тему:</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

find_pyqt = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>615</width>
    <height>344</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Поиск</string>
  </property>
  <widget class="QTableWidget" name="find_table">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>90</y>
     <width>591</width>
     <height>241</height>
    </rect>
   </property>
  </widget>
  <widget class="QWidget" name="horizontalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>591</width>
     <height>61</height>
    </rect>
   </property>
   <layout class="QHBoxLayout" name="horizontalLayout">
    <item>
     <widget class="QLineEdit" name="lineEdit"/>
    </item>
    <item>
     <widget class="QComboBox" name="comboBox"/>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton">
      <property name="text">
       <string>Найти</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

add_pyqt = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>AddMovieDialog</class>
 <widget class="QDialog" name="AddMovieDialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Добавить фильм или сериал</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <layout class="QFormLayout" name="formLayout">
     <item row="0" column="0">
      <widget class="QLabel" name="labelTitle">
       <property name="text">
        <string>Название:</string>
       </property>
      </widget>
     </item>
     <item row="0" column="1">
      <widget class="QLineEdit" name="lineEditTitle"/>
     </item>
     <item row="1" column="0">
      <widget class="QLabel" name="labelType">
       <property name="text">
        <string>Тип:</string>
       </property>
      </widget>
     </item>
     <item row="1" column="1">
      <widget class="QComboBox" name="comboBoxType"/>
     </item>
     <item row="2" column="0">
      <widget class="QLabel" name="labelYear">
       <property name="text">
        <string>Год выпуска:</string>
       </property>
      </widget>
     </item>
     <item row="2" column="1">
      <widget class="QSpinBox" name="spinBoxYear">
       <property name="minimum">
        <number>1900</number>
       </property>
       <property name="maximum">
        <number>2100</number>
       </property>
       <property name="value">
        <number>2024</number>
       </property>
      </widget>
     </item>
     <item row="3" column="0">
      <widget class="QLabel" name="labelGenre">
       <property name="text">
        <string>Жанр:</string>
       </property>
      </widget>
     </item>
     <item row="3" column="1">
      <widget class="QLineEdit" name="lineEditGenre"/>
     </item>
     <item row="4" column="0">
      <widget class="QLabel" name="labelDirector">
       <property name="text">
        <string>Режиссер:</string>
       </property>
      </widget>
     </item>
     <item row="4" column="1">
      <widget class="QLineEdit" name="lineEditDirector"/>
     </item>
     <item row="5" column="0">
      <widget class="QLabel" name="labelRating">
       <property name="text">
        <string>Оценка:</string>
       </property>
      </widget>
     </item>
     <item row="5" column="1">
      <widget class="QDoubleSpinBox" name="doubleSpinBoxRating">
       <property name="minimum">
        <double>0.000000000000000</double>
       </property>
       <property name="maximum">
        <double>10.000000000000000</double>
       </property>
       <property name="singleStep">
        <double>0.100000000000000</double>
       </property>
      </widget>
     </item>
     <item row="6" column="0">
      <widget class="QLabel" name="labelStatus">
       <property name="text">
        <string>Статус:</string>
       </property>
      </widget>
     </item>
     <item row="6" column="1">
      <widget class="QComboBox" name="comboBoxStatus"/>
     </item>
    </layout>
   </item>
   <item>
    <layout class="QHBoxLayout" name="buttonLayout">
     <item>
      <widget class="QPushButton" name="buttonAdd">
       <property name="text">
        <string>Добавить</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="buttonCancel">
       <property name="text">
        <string>Отмена</string>
       </property>
      </widget>
     </item>
    </layout>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

info_pyqt = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>452</width>
    <height>653</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Документация</string>
  </property>
  <widget class="QLabel" name="photo">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>-10</y>
     <width>391</width>
     <height>161</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QTextEdit" name="textEdit">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>140</y>
     <width>451</width>
     <height>511</height>
    </rect>
   </property>
   <property name="html">
    <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;                      1.	&lt;/span&gt;&lt;span style=&quot; font-family:'.SF NS'; font-weight:600; color:#fc0107;&quot;&gt;Меню «Настройки»&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	Доступ к изменениям темы, добавлению новых фильмов и просмотру избранных.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	2.	&lt;/span&gt;&lt;span style=&quot; font-family:'.SF NS'; font-weight:600; color:#fc0107;&quot;&gt;Поисковая строка и фильтр&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	Введите название фильма/сериала и настройте фильтры (по жанру, году и статусу).&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	Нажмите кнопку «Найти», чтобы получить результаты.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	3.	&lt;/span&gt;&lt;span style=&quot; font-family:'.SF NS'; font-weight:600; color:#fc0107;&quot;&gt;Кнопки управления&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	&lt;/span&gt;&lt;span style=&quot; font-family:'.SF NS'; font-weight:600; color:#fc0107;&quot;&gt;«Выход»&lt;/span&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;: Завершает работу приложения после подтверждения.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	&lt;/span&gt;&lt;span style=&quot; font-family:'.SF NS'; font-weight:600; color:#fc0107;&quot;&gt;«Info»&lt;/span&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;: Открывает окно с документацией приложения.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;		&lt;/span&gt;&lt;span style=&quot; font-family:'.SF NS'; font-weight:600; color:#fc0107;&quot;&gt;Кнопка с числом&lt;/span&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;: Открывает окно с фильмами, которые уже просмотрены, но еще не 				оценены.		&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;		&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	4.	&lt;/span&gt;&lt;span style=&quot; font-family:'.SF NS'; font-weight:600; color:#fc0107;&quot;&gt;Список «В процессе»&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	Автоматически отображает фильмы, у которых установлен статус «В процессе».&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;&lt;br /&gt;&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; font-weight:600; color:#fc0107;&quot;&gt;Настройки приложения&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;&lt;br /&gt;&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; font-weight:600; color:#fc0107;&quot;&gt;Изменение темы&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;&lt;br /&gt;&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	1.	Перейдите в меню «Настройки» → «Тема».&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	2.	В открывшемся диалоговом окне выберите нужную тему (светлая или тёмная).&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;&lt;br /&gt;&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; font-weight:600; color:#fc0107;&quot;&gt;Добавление фильма/сериала&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;&lt;br /&gt;&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	1.	Перейдите в меню «Настройки» → «Добавить».&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	2.	Введите информацию о фильме:&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	Название.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;		Тип.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;		Год выпуска.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	Жанр.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	Режиссер&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;		Оценка(шаг в 0.1. Максимольно 10)&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	Установите статус: «Не просмотрено», «В процессе», «Просмотрено».&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	3.	Нажмите «Добавить». Новый фильм появится в соответствующем списке.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;		Нажмите &amp;quot;Отмена&amp;quot;. Окно закроется&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;&lt;br /&gt;&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; font-weight:600; color:#fc0107;&quot;&gt;Работа с избранными&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;&lt;br /&gt;&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	1.	Перейдите в меню «Настройки» → «Избранные».&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	2.	В открывшемся списке отображаются фильмы, помеченные как избранные.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	3.	Для добавления/удаления фильма из избранного:&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	Найдите фильм в любом списке приложения.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	Поставьте или снимите галочку в поле «Избранное» рядом с ним.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;&lt;br /&gt;&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; font-weight:600; color:#fc0107;&quot;&gt;4. Поиск фильмов&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;&lt;br /&gt;&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	1.	Введите название фильма/сериала в строку поиска.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	2.	Настройте фильтры (опционально):&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	Название.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;		Тип.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;		Год выпуска.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	Жанр.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	Режиссер&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;		Оценка&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;		Статус(На каком этапе фильм)&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;		Избранные&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;		Комментарии&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	3.	Нажмите кнопку «Найти». Откроется диалоговое окно с результатами.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	4.	Для редактирования фильма или сериала дважды кликните на его название в списке.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;&lt;br /&gt;&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; font-weight:600; color:#fc0107;&quot;&gt;5. Работа со статусами фильмов&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;&lt;br /&gt;&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; font-weight:600; color:#fc0107;&quot;&gt;Изменение статуса фильма&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;&lt;br /&gt;&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	1.	Найдите фильм в списке.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	2.	Выберите нужный статус из выпадающего списка:&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	«Не просмотрено».&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	«В процессе».&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	«Просмотрено».&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	3.	После изменения статус автоматически сохранится, и списки обновятся.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;&lt;br /&gt;&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; font-weight:600; color:#fc0107;&quot;&gt;6. Редактирование фильма&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;&lt;br /&gt;&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	1.	Найдите фильм в любом списке.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	2.	Дважды кликните по его названию.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	3.	В открывшемся окне редактирования измените нужные поля:&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	Название.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;		Тип.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;		Год выпуска.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	Жанр.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	Режиссер&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;		Оценка&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;		Комментарии&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	4.	Нажмите «Сохранить». Изменения отразятся во всех списках.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;		Нажмите &amp;quot;Удалить&amp;quot;. Фильм или сериал удалится из db.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;&lt;br /&gt;&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; font-weight:600; color:#fc0107;&quot;&gt;7. Завершение работы приложения&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;&lt;br /&gt;&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	1.	Нажмите кнопку «Выход» в главном окне.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:21px; margin-right:0px; -qt-block-indent:0; text-indent:-21px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	2.	В появившемся диалоговом окне выберите:&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	&lt;/span&gt;&lt;span style=&quot; font-family:'.SF NS'; font-weight:600; color:#fc0107;&quot;&gt;Yes&lt;/span&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;, чтобы завершить работу приложения.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;	•	&lt;/span&gt;&lt;span style=&quot; font-family:'.SF NS'; font-weight:600; color:#fc0107;&quot;&gt;No&lt;/span&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;, чтобы вернуться к работе.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:0px; margin-left:33px; margin-right:0px; -qt-block-indent:0; text-indent:-33px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;&lt;br /&gt;&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; font-weight:600; color:#fc0107;&quot;&gt;8. Автоматическое сохранение&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;&lt;br /&gt;&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;Все изменения (добавление фильмов, выставление оценок, изменения статуса) автоматически сохраняются в базе данных &lt;/span&gt;&lt;span style=&quot; font-family:'.AppleSystemUIFontMonospaced'; color:#fc0107;&quot;&gt;top100.db&lt;/span&gt;&lt;span style=&quot; font-family:'.SF NS'; color:#fc0107;&quot;&gt;.&lt;/span&gt;&lt;span style=&quot; color:#fc0107;&quot;&gt; &lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

redactor_pyqt = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>471</width>
    <height>427</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Редактирование</string>
  </property>
  <widget class="QWidget" name="layoutWidget">
   <property name="geometry">
    <rect>
     <x>7</x>
     <y>10</y>
     <width>451</width>
     <height>221</height>
    </rect>
   </property>
   <layout class="QFormLayout" name="formLayout">
    <item row="0" column="0">
     <widget class="QLabel" name="labelTitle">
      <property name="text">
       <string>Название:</string>
      </property>
     </widget>
    </item>
    <item row="0" column="1">
     <widget class="QLineEdit" name="lineEditTitle"/>
    </item>
    <item row="1" column="0">
     <widget class="QLabel" name="labelType">
      <property name="text">
       <string>Тип:</string>
      </property>
     </widget>
    </item>
    <item row="1" column="1">
     <widget class="QComboBox" name="comboBoxType"/>
    </item>
    <item row="2" column="0">
     <widget class="QLabel" name="labelYear">
      <property name="text">
       <string>Год выпуска:</string>
      </property>
     </widget>
    </item>
    <item row="2" column="1">
     <widget class="QSpinBox" name="spinBoxYear">
      <property name="minimum">
       <number>1900</number>
      </property>
      <property name="maximum">
       <number>2100</number>
      </property>
      <property name="value">
       <number>2024</number>
      </property>
     </widget>
    </item>
    <item row="3" column="0">
     <widget class="QLabel" name="labelGenre">
      <property name="text">
       <string>Жанр:</string>
      </property>
     </widget>
    </item>
    <item row="3" column="1">
     <widget class="QLineEdit" name="lineEditGenre"/>
    </item>
    <item row="4" column="0">
     <widget class="QLabel" name="labelDirector">
      <property name="text">
       <string>Режиссер:</string>
      </property>
     </widget>
    </item>
    <item row="4" column="1">
     <widget class="QLineEdit" name="lineEditDirector"/>
    </item>
    <item row="5" column="0">
     <widget class="QLabel" name="labelRating">
      <property name="text">
       <string>Оценка:</string>
      </property>
     </widget>
    </item>
    <item row="5" column="1">
     <widget class="QDoubleSpinBox" name="doubleSpinBoxRating">
      <property name="minimum">
       <double>0.000000000000000</double>
      </property>
      <property name="maximum">
       <double>10.000000000000000</double>
      </property>
      <property name="singleStep">
       <double>0.100000000000000</double>
      </property>
     </widget>
    </item>
    <item row="6" column="0">
     <widget class="QLabel" name="labelStatus">
      <property name="text">
       <string>Статус:</string>
      </property>
     </widget>
    </item>
    <item row="6" column="1">
     <widget class="QComboBox" name="comboBoxStatus"/>
    </item>
   </layout>
  </widget>
  <widget class="QPushButton" name="buttonDelete">
   <property name="geometry">
    <rect>
     <x>340</x>
     <y>380</y>
     <width>111</width>
     <height>32</height>
    </rect>
   </property>
   <property name="text">
    <string>Удалить</string>
   </property>
  </widget>
  <widget class="QPushButton" name="buttonSave">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>380</y>
     <width>141</width>
     <height>32</height>
    </rect>
   </property>
   <property name="text">
    <string>Сохранить</string>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>240</y>
     <width>151</width>
     <height>21</height>
    </rect>
   </property>
   <property name="text">
    <string>Добавьте комментарий:</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="commentEditTitle">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>270</y>
     <width>431</width>
     <height>101</height>
    </rect>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

favorite_pyqt = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>559</width>
    <height>395</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Избранные</string>
  </property>
  <widget class="QTableWidget" name="favorite_table">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>561</width>
     <height>391</height>
    </rect>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

score_pyqt = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>559</width>
    <height>395</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Ждут оценки:</string>
  </property>
  <widget class="QTableWidget" name="score_table">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>561</width>
     <height>391</height>
    </rect>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        f_main = io.StringIO(main_pyqt)
        uic.loadUi(f_main, self)  # Загрузка интерфейса из строки main_pyqt

        self.current_theme = "white"  # Установка текущей темы
        self.apply_theme()  # Применение темы

        # Подключение к базе данных
        self.conn = sqlite3.connect("top100.db")
        self.cursor = self.conn.cursor()
        self.updateButton()  # Обновление кнопки с количеством фильмов без оценки

        # Инициализация UI
        self.lineEdit.setPlaceholderText('Поиск:')  # Установка текста-подсказки в поле поиска
        self.column_selector.addItem("   ")  # Добавление пустого фильтра в список фильтров
        self.column_selector.addItems(self.get_columns())  # Добавление названий колонок таблицы
        self.find_button.clicked.connect(self.find)  # Привязка кнопки поиска к функции find

        self.setup_menu()  # Настройка меню

        # Настройка таблицы
        self.progress_table.setColumnCount(3)
        self.progress_table.setHorizontalHeaderLabels(["Название", "Статус", "Избранные"])  # Установка заголовков колонок
        self.update_table()  # Заполнение таблицы данными

        # Привязка кнопок к соответствующим функциям
        self.exitbutton.clicked.connect(self.exit)  # Выход
        self.infobutton.clicked.connect(self.info)  # Информация
        self.films_score_button.clicked.connect(self.score)  # Оценка фильмов

        # Обработка изменения элемента таблицы (для обновления избранных)
        self.progress_table.itemChanged.connect(self.update_favorite_status)

    def setup_menu(self):
        """Настраивает меню приложения"""
        menu = self.menuBar()
        menu.setNativeMenuBar(False)
        file_menu = menu.addMenu("Настройки")

        # Действие для изменения темы
        theme_action = QAction("Тема", self)
        theme_action.triggered.connect(self.background)
        file_menu.addAction(theme_action)

        # Действие для добавления фильма
        add_action = QAction("Добавить", self)
        add_action.triggered.connect(self.add)
        file_menu.addAction(add_action)

        # Действие для отображения избранных фильмов
        favorite_action = QAction('Избранные', self)
        favorite_action.triggered.connect(self.favorite)
        file_menu.addAction(favorite_action)

    def get_columns(self):
        """Получает список колонок таблицы Movies"""
        self.cursor.execute("PRAGMA table_info(Movies)")
        return [col[1] for col in self.cursor.fetchall()]

    def apply_theme(self):
        """Применяет текущую тему"""
        themes = {
            "white": "",  # Стандартная светлая тема
            "black": '''
                MainWindow { background-color: #121212; }
                QWidget { background-color: #1E1E1E; color: #E0E0E0; }
                QPushButton { background-color: #37474F; color: #80DEEA; border: 1px solid #455A64; border-radius: 5px; }
                QPushButton:hover { background-color: #455A64; }
                QTableWidget { background-color: #1E1E1E; color: #E0E0E0; border: 1px solid #424242; }
                QDialog { background-color: #1E1E1E; }
            '''
        }
        self.setStyleSheet(themes.get(self.current_theme, ""))  # Применение стиля на основе текущей темы

    def info(self):
        """Открывает окно информации"""
        InfoWindow(self).exec()

    def add(self):
        """Открывает окно добавления фильма"""
        AddWindow(self).exec()

    def background(self):
        """Открывает окно для выбора темы оформления"""
        BackgroundWindow(self).exec()

    def open_redactor_window(self, this_window, index, table):
        """Открывает окно редактирования выбранного фильма"""
        row = index.row()  # Получаем номер строки
        movie_title_item = table.item(row, 0)  # Получаем элемент первой ячейки (Название фильма)
        self.this_window = this_window

        if movie_title_item:
            movie_title = movie_title_item.text()  # Получаем название фильма
            self.cursor.execute("SELECT * FROM Movies WHERE Название = ?", (movie_title,))
            movie_data = self.cursor.fetchone()  # Получаем данные фильма из базы данных

            if movie_data:
                # Открываем окно редактирования с переданными данными
                redactor_window = RedactorWindow(self, this_window, movie_data)
                redactor_window.exec()

    def find(self):
        """Открывает окно поиска фильмов"""
        query = self.lineEdit.text().strip()  # Получение строки поиска
        selected_filter = self.column_selector.currentText()  # Получение выбранного фильтра
        self.find_window = FindWindow(self, query, selected_filter)
        self.find_window.exec()

    def favorite(self):
        """Открывает окно избранных фильмов"""
        self.favorite_window = FavoriteWindow(self)
        self.favorite_window.exec()

    def score(self):
        """Открывает окно оценки фильмов"""
        self.score_window = ScoreWindow(self)
        self.score_window.exec()

    def exit(self):
        """Закрывает приложение с подтверждением"""
        response = QMessageBox.question(self, 'Подтвердите', 'Вы точно хотите выйти?',
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                        QMessageBox.StandardButton.No)

        if response == QMessageBox.StandardButton.Yes:
            QApplication.quit()  # Завершение работы приложения
            self.conn.close()  # Закрытие соединения с базой данных

    def update_table(self):
        """Обновляет таблицу с фильмами"""
        self.cursor.execute("SELECT Название, Статус, Избранные FROM Movies WHERE Статус = 'В процессе'")
        rows = self.cursor.fetchall()

        self.progress_table.setRowCount(len(rows))  # Установка количества строк таблицы
        for row_idx, (title, status, is_favorite) in enumerate(rows):
            # Установка данных в ячейки
            self.progress_table.setItem(row_idx, 0, QTableWidgetItem(title))  # Название фильма

            # Создание выпадающего списка для статуса
            status_combobox = QComboBox()
            status_combobox.addItems(["Не просмотрено", "В процессе", "Просмотрено"])
            status_combobox.setCurrentText(status or "Не просмотрено")
            status_combobox.currentTextChanged.connect(
                lambda s, row=row_idx: self.update_status(s, row)  # Связывание изменения с функцией обновления
            )
            self.progress_table.setCellWidget(row_idx, 1, status_combobox)

            # Создание чекбокса для избранных
            favorite_checkbox = QTableWidgetItem()
            favorite_checkbox.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
            favorite_checkbox.setCheckState(Qt.CheckState.Checked if is_favorite else Qt.CheckState.Unchecked)
            self.progress_table.setItem(row_idx, 2, favorite_checkbox)

        # Настройка столбцов
        self.progress_table.horizontalHeader().setStretchLastSection(True)
        self.progress_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.progress_table.resizeColumnsToContents()
        self.progress_table.resizeRowsToContents()

        # Обработчик двойного клика для открытия окна редактирования
        self.progress_table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.progress_table.doubleClicked.connect(lambda index: self.open_redactor_window(self, index, self.progress_table))

    def update_status(self, new_status, row_idx):
        """Обновляет статус фильма"""
        movie_title = self.progress_table.item(row_idx, 0).text()  # Получение названия фильма
        self.cursor.execute("UPDATE Movies SET Статус = ? WHERE Название = ?", (new_status, movie_title))
        self.conn.commit()  # Сохранение изменений
        self.update_table()  # Обновление таблицы
        self.updateButton()  # Обновление кнопки

    def update_favorite_status(self, item):
        """Обновляет статус избранного для фильма"""
        row = item.row()
        col = item.column()
        if col == 2:  # Если изменение произошло в колонке избранных
            movie_title = self.progress_table.item(row, 0).text()  # Получение названия фильма
            is_favorite = item.checkState() == Qt.CheckState.Checked  # Проверка состояния чекбокса
            self.cursor.execute("UPDATE Movies SET Избранные = ? WHERE Название = ?", (is_favorite, movie_title))
            self.conn.commit()  # Сохранение изменений

    def updateButton(self):
        """Обновляет текст кнопки для оценки фильмов"""
        self.cursor.execute("SELECT COUNT(*) FROM Movies WHERE Оценка = 0 AND Статус = 'Просмотрено'")
        count = self.cursor.fetchone()[0]  # Получение количества фильмов без оценки
        self.films_score_button.setText(str(count))  # Установка числа в кнопку

class InfoWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()
        # Сохраняем ссылку на главное окно
        self.main_window = main_window

        # Загружаем интерфейс из строки
        f_info = io.StringIO(info_pyqt)
        uic.loadUi(f_info, self)

        # Загружаем изображение и изменяем его размер, чтобы он подошел под виджет
        pixmap = QPixmap('чиловыйпарень.jpg')
        scaled_pixmap = pixmap.scaled(self.photo.size(), Qt.AspectRatioMode.KeepAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        # Устанавливаем изображение в виджет
        self.photo.setPixmap(scaled_pixmap)

        # Применяем тему
        self.apply_theme()

    def apply_theme(self):
        """Применяет тему из главного окна"""
        self.setStyleSheet(self.main_window.styleSheet())

class AddWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()
        # Сохраняем ссылку на главное окно
        self.main_window = main_window

        # Загружаем интерфейс из строки
        f_add = io.StringIO(add_pyqt)
        uic.loadUi(f_add, self)

        # Заполняем выпадающие списки для типа и статуса
        self.comboBoxType.addItems(["Фильм", "Сериал"])
        self.comboBoxStatus.addItems(["Не просмотрено", "В процессе", "Просмотрено"])

        # Привязка кнопок
        self.buttonAdd.clicked.connect(self.on_add)  # Кнопка добавления
        self.buttonCancel.clicked.connect(self.reject)  # Кнопка отмены

        # Применяем тему
        self.apply_theme()

    def on_add(self):
        """Обработчик для добавления фильма в базу данных"""
        # Считываем данные с формы
        title = self.lineEditTitle.text().strip()
        type_ = self.comboBoxType.currentText()
        year = self.spinBoxYear.value()
        genre = self.lineEditGenre.text().strip()
        director = self.lineEditDirector.text().strip()
        rating = self.doubleSpinBoxRating.value()
        status = self.comboBoxStatus.currentText()

        # Проверка на обязательные поля
        if not title or not genre or not director:
            QMessageBox.warning(self, "Ошибка", "Поля 'Название', 'Жанр' и 'Режиссер' не могут быть пустыми.")
            return

        # Добавляем фильм в базу данных и показываем сообщение об успехе
        self.add_movie_to_db(title, type_, year, genre, director, rating, status)
        QMessageBox.information(self, "Успех", f"Добавлено: {title}")
        self.accept()  # Закрываем окно
        # Обновляем таблицу в главном окне
        self.main_window.update_table()
        self.main_window.updateButton()

    def add_movie_to_db(self, title, type_, year, genre, director, rating, status):
        """Добавляет фильм в базу данных"""
        conn = sqlite3.connect("top100.db")
        cursor = conn.cursor()

        # Создаем таблицу, если она еще не существует
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS movies (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Название TEXT,
                        Тип TEXT,
                        Год INTEGER,
                        Жанр TEXT,
                        Режиссер TEXT,
                        Оценка REAL,
                        Статус TEXT
                    )
                ''')

        # Вставляем данные о фильме в таблицу
        cursor.execute('''
                    INSERT INTO movies (Название, Тип, Год, Жанр, Режиссер, Оценка, Статус)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (title, type_, year, genre, director, rating, status))

        conn.commit()  # Сохраняем изменения в базе данных
        conn.close()  # Закрываем соединение с базой данных

    def apply_theme(self):
        """Применяет тему из главного окна"""
        self.setStyleSheet(self.main_window.styleSheet())

class BackgroundWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()
        # Сохраняем ссылку на главное окно
        self.main_window = main_window

        # Загружаем интерфейс из строки
        f_background = io.StringIO(background_pyqt)
        uic.loadUi(f_background, self)

        # Применяем тему
        self.apply_theme()

        # Устанавливаем текущую тему (по умолчанию белая или черная)
        if self.main_window.current_theme == "white":
            self.white.setChecked(True)
        elif self.main_window.current_theme == "black":
            self.black.setChecked(True)

        # Привязываем обработчики для выбора темы
        self.white.clicked.connect(self.white_background)  # Белая тема
        self.black.clicked.connect(self.black_background)  # Черная тема

    def white_background(self):
        """Устанавливает белую тему"""
        self.main_window.current_theme = "white"  # Обновляем текущую тему в главном окне
        self.main_window.apply_theme()  # Применяем тему к главному окну
        self.apply_theme()  # Применяем тему к текущему окну

    def black_background(self):
        """Устанавливает черную тему"""
        self.main_window.current_theme = "black"  # Обновляем текущую тему в главном окне
        self.main_window.apply_theme()  # Применяем тему к главному окну
        self.apply_theme()  # Применяем тему к текущему окну

    def apply_theme(self):
        """Применяет текущую тему"""
        self.setStyleSheet(self.main_window.styleSheet())  # Устанавливаем стиль, соответствующий текущей теме


class RedactorWindow(QDialog):
    def __init__(self, main_window, this_window, movie_data):
        super().__init__()
        # Загружаем интерфейс из строки
        f_redactor = io.StringIO(redactor_pyqt)
        uic.loadUi(f_redactor, self)

        # Сохраняем ссылки на главное окно и окно, из которого был вызван редактор
        self.main_window = main_window
        self.this_window = this_window
        self.movie_data = movie_data  # Данные фильма, переданные в редактор

        # Применяем текущую тему
        self.apply_theme()

        # Инициализируем элементы управления
        self.comboBoxType.addItems(["Фильм", "Сериал"])
        self.comboBoxStatus.addItems(["Не просмотрено", "Просмотрено", "В процессе"])

        # Заполняем поля формы значениями, соответствующими текущему фильму
        self.lineEditTitle.setText(self.movie_data[0])  # Название фильма
        self.comboBoxType.setCurrentText(self.movie_data[1])  # Тип (фильм/сериал)
        self.spinBoxYear.setValue(self.movie_data[2])  # Год выпуска
        self.lineEditGenre.setText(self.movie_data[3])  # Жанр
        self.lineEditDirector.setText(self.movie_data[4])  # Режиссёр
        self.doubleSpinBoxRating.setValue(self.movie_data[5])  # Оценка
        self.comboBoxStatus.setCurrentText(self.movie_data[6])  # Статус
        self.commentEditTitle.setText(self.movie_data[8])  # Комментарии

        # Привязываем обработчики для кнопок
        self.buttonSave.clicked.connect(self.save_changes)  # Сохранить изменения
        self.buttonDelete.clicked.connect(self.delete_movie)  # Удалить фильм

    def save_changes(self):
        """Сохраняет изменения фильма в базе данных"""
        # Получаем значения из полей ввода
        title = self.lineEditTitle.text().strip()
        type_ = self.comboBoxType.currentText()
        year = self.spinBoxYear.value()
        genre = self.lineEditGenre.text().strip()
        director = self.lineEditDirector.text().strip()
        rating = self.doubleSpinBoxRating.value()
        status = self.comboBoxStatus.currentText()
        comment_ = self.commentEditTitle.text().strip()

        # Проверка на обязательные поля
        if not title or not genre or not director:
            QMessageBox.warning(self, "Ошибка", "Поля 'Название', 'Жанр' и 'Режиссёр' не могут быть пустыми.")
            return

        # Обновление фильма в базе данных
        self.update_movie_in_db(title, type_, year, genre, director, rating, status, comment_)
        QMessageBox.information(self, "Успех", f"Изменено: {title}")

        # Обновляем таблицы в главном и исходном окне
        self.main_window.updateButton()
        self.this_window.update_table()

        self.accept()

    def update_movie_in_db(self, title, type_, year, genre, director, rating, status, comment_):
        """Обновляет данные фильма в базе данных"""
        conn = sqlite3.connect("top100.db")
        cursor = conn.cursor()

        # Выполняем запрос на обновление данных фильма
        cursor.execute('''
            UPDATE Movies
            SET Название = ?, Тип = ?, Год = ?, Жанр = ?, Режиссер = ?, Оценка = ?, Статус = ?, Комментарии = ?
            WHERE Название = ?
        ''', (title, type_, year, genre, director, rating, status, comment_, self.movie_data[0]))

        conn.commit()  # Сохраняем изменения в базе данных
        conn.close()  # Закрываем соединение

    def delete_movie(self):
        """Удаляет фильм из базы данных"""
        movie_title = self.lineEditTitle.text().strip()
        if not movie_title:
            QMessageBox.warning(self, "Ошибка", "Название фильма не может быть пустым.")
            return

        # Подтверждение удаления
        response = QMessageBox.question(self, 'Подтвердите', f'Вы хотите удалить фильм "{movie_title}"?',
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                        QMessageBox.StandardButton.No)

        if response == QMessageBox.StandardButton.Yes:
            # Выполняем удаление фильма из базы данных
            conn = sqlite3.connect("top100.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Movies WHERE Название = ?", (movie_title,))
            conn.commit()  # Сохраняем изменения
            conn.close()  # Закрываем соединение

            # Информируем пользователя об успешном удалении
            QMessageBox.information(self, "Удаление", f"Фильм '{movie_title}' был успешно удален.")

            # Обновляем таблицы
            self.main_window.update_table()
            if self.main_window != self.this_window:
                self.this_window.update_table()
            self.main_window.updateButton()

            self.accept()

    def apply_theme(self):
        """Применяет текущую тему"""
        self.setStyleSheet(self.main_window.styleSheet())  # Устанавливаем стиль, соответствующий текущей теме

class FindWindow(QDialog):
    def __init__(self, main_window, query, selected_filter):
        super().__init__()
        self.main_window = main_window
        f_find = io.StringIO(find_pyqt)
        uic.loadUi(f_find, self)

        self.cursor = self.main_window.cursor
        self.conn = self.main_window.conn

        # Получаем все столбцы из базы данных
        self.columns = self.main_window.get_columns()

        # Инициализируем комбобокс с фильтром
        self.comboBox.addItem("   ")  # Добавляем пустой элемент для поиска по всем столбцам
        self.comboBox.addItems(self.columns)  # Добавляем все столбцы в комбобокс
        self.comboBox.setCurrentText(selected_filter)  # Устанавливаем выбранный фильтр

        # Устанавливаем текст для строки поиска
        self.lineEdit.setText(query)  # Устанавливаем исходный запрос в строку поиска
        self.pushButton.clicked.connect(self.update_table)  # Привязываем обработчик к кнопке

        self.apply_theme()  # Применяем тему оформления
        self.update_table()  # Выполняем поиск сразу при открытии окна

    def update_table(self):
        """Выполняет поиск фильмов в базе данных"""
        search_text = self.lineEdit.text().strip().capitalize()  # Получаем текст поиска
        selected_column = self.comboBox.currentText()  # Получаем выбранный фильтр
        self.main_window.lineEdit.setText(self.lineEdit.text().strip())  # Обновляем строку поиска в главном окне

        if search_text:  # Если введен текст для поиска
            if selected_column == "   ":  # Если не выбран конкретный столбец, ищем по всем столбцам
                conditions = " OR ".join(
                    [f"{col} LIKE ? COLLATE NOCASE" for col in self.columns]
                )
                params = [f"%{search_text}%"] * len(self.columns)
            else:  # Ищем только по выбранному столбцу
                conditions = f"{selected_column} LIKE ? COLLATE NOCASE"
                params = [f"%{search_text}%"]

            # Выполняем запрос к базе данных
            query = f"SELECT * FROM Movies WHERE {conditions}"
            self.cursor.execute(query, params)
            results = self.cursor.fetchall()

            # Заполняем таблицу результатами поиска
            self.find_table.setRowCount(len(results))  # Устанавливаем количество строк
            self.find_table.setColumnCount(len(self.columns))  # Устанавливаем количество столбцов
            self.find_table.setHorizontalHeaderLabels(self.columns)  # Устанавливаем заголовки столбцов

            # Заполняем таблицу данными
            for row_idx, row_data in enumerate(results):
                for col_idx, value in enumerate(row_data):
                    if self.columns[col_idx] == "Статус":
                        # Для колонки "Статус" добавляем выпадающий список
                        combo_box = QComboBox(self)
                        combo_box.addItems(["Не просмотрено", "В процессе", "Просмотрено"])
                        combo_box.setCurrentText(str(value))  # Устанавливаем текущий статус фильма
                        combo_box.currentTextChanged.connect(
                            lambda new_status, r=row_idx: self.update_status(r, new_status)
                        )
                        self.find_table.setCellWidget(row_idx, col_idx, combo_box)

                    elif self.columns[col_idx] == "Избранные":
                        # Для колонки "Избранные" добавляем чекбокс
                        favorite_checkbox = QTableWidgetItem()
                        favorite_checkbox.setCheckState(Qt.CheckState.Checked if value else Qt.CheckState.Unchecked)
                        favorite_checkbox.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                        self.find_table.setItem(row_idx, col_idx, favorite_checkbox)

                    else:
                        # Для всех остальных колонок заполняем обычные ячейки
                        item = QTableWidgetItem(str(value))
                        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Делаем ячейку не редактируемой
                        self.find_table.setItem(row_idx, col_idx, item)

            # Настройки отображения таблицы
            self.find_table.horizontalHeader().setStretchLastSection(True)  # Растягиваем последний столбец
            self.find_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)  # Автоматическое растягивание столбцов
            self.find_table.resizeColumnsToContents()  # Подбираем ширину столбцов по содержимому
            self.find_table.resizeRowsToContents()  # Подбираем высоту строк по содержимому

            # Подключаем обработчик для изменения состояния чекбоксов
            self.find_table.itemChanged.connect(self.update_favorite_status)
            self.find_table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)  # Отключаем выделение строк
            self.find_table.doubleClicked.connect(
                lambda index: self.main_window.open_redactor_window(self, index, self.find_table)  # Действие при двойном клике на строку
            )

    def update_status(self, row_idx, new_status):
        """Обновляет статус фильма в базе данных"""
        title_item = self.find_table.item(row_idx, self.columns.index("Название"))
        if title_item:
            movie_title = title_item.text()
            self.cursor.execute("UPDATE Movies SET Статус = ? WHERE Название = ?", (new_status, movie_title))
            self.conn.commit()  # Применяем изменения в базе данных
            self.main_window.update_table()  # Обновляем таблицу на главном экране
            self.main_window.updateButton()  # Обновляем кнопки на главном экране

    def update_favorite_status(self, item):
        """Обновляет статус 'Избранные' в базе данных"""
        row = item.row()
        col = item.column()

        if col == self.columns.index("Избранные"):  # Проверяем, что обновляется колонка "Избранные"
            movie_title = self.find_table.item(row, self.columns.index("Название")).text()
            is_favorite = item.checkState() == Qt.CheckState.Checked  # Получаем состояние чекбокса
            self.cursor.execute("UPDATE Movies SET Избранные = ? WHERE Название = ?", (is_favorite, movie_title))
            self.conn.commit()  # Применяем изменения в базе данных
            self.main_window.update_table()  # Обновляем таблицу на главном экране

    def apply_theme(self):
        """Применяет тему оформления из главного окна"""
        self.setStyleSheet(self.main_window.styleSheet())


class FavoriteWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        f_favorite = io.StringIO(favorite_pyqt)  # Загрузка UI из строки
        uic.loadUi(f_favorite, self)

        self.apply_theme()  # Применяем текущую тему
        self.update_table()  # Обновляем таблицу при открытии окна

    def update_table(self):
        self.cursor = self.main_window.cursor
        self.conn = self.main_window.conn

        # Указываем только нужные столбцы для отображения
        self.selected_columns = ["Название", "Жанр", "Режиссер", "Статус", "Избранные"]
        # Выполняем запрос на выборку фильмов, которые находятся в "Избранных"
        self.cursor.execute(f"SELECT {', '.join(self.selected_columns)} FROM Movies WHERE Избранные = 1")
        rows = self.cursor.fetchall()  # Получаем все строки

        self.favorite_table.setRowCount(len(rows))  # Устанавливаем количество строк в таблице
        self.favorite_table.setColumnCount(len(self.selected_columns))  # Устанавливаем количество столбцов
        self.favorite_table.setHorizontalHeaderLabels(self.selected_columns)  # Устанавливаем заголовки столбцов

        # Заполняем таблицу данными
        for row_idx, row_data in enumerate(rows):
            for col_idx, value in enumerate(row_data):
                column_name = self.selected_columns[col_idx]
                if column_name == "Статус":
                    # Для колонки "Статус" добавляем выпадающий список
                    combo_box = QComboBox(self)
                    combo_box.addItems(["Не просмотрено", "В процессе", "Просмотрено"])
                    combo_box.setCurrentText(str(value))  # Устанавливаем текущий статус фильма
                    combo_box.currentTextChanged.connect(
                        lambda new_status, r=row_idx: self.update_status(r, new_status)  # Обработчик изменения статуса
                    )
                    self.favorite_table.setCellWidget(row_idx, col_idx, combo_box)

                elif column_name == "Избранные":
                    # Для колонки "Избранные" создаём чекбокс
                    favorite_checkbox = QTableWidgetItem()
                    favorite_checkbox.setCheckState(Qt.CheckState.Checked if value else Qt.CheckState.Unchecked)
                    favorite_checkbox.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)  # Сделаем чекбокс доступным для изменения
                    self.favorite_table.setItem(row_idx, col_idx, favorite_checkbox)

                else:
                    # Для всех остальных колонок просто создаём не редактируемый элемент таблицы
                    item = QTableWidgetItem(str(value))
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Делаем ячейки не редактируемыми
                    self.favorite_table.setItem(row_idx, col_idx, item)

        # Настройки отображения таблицы
        self.favorite_table.horizontalHeader().setStretchLastSection(True)  # Растягиваем последний столбец
        self.favorite_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)  # Автоматически растягиваем столбцы
        self.favorite_table.resizeColumnsToContents()  # Подбираем ширину столбцов по содержимому
        self.favorite_table.resizeRowsToContents()  # Подбираем высоту строк по содержимому

        self.favorite_table.itemChanged.connect(self.update_favorite_status)  # Обработчик изменения состояния чекбокса
        self.favorite_table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)  # Отключаем возможность выделения строк
        # Действие при двойном клике на строку — открытие редактора
        self.favorite_table.doubleClicked.connect(
            lambda index: self.main_window.open_redactor_window(self, index, self.favorite_table)
        )

    def update_status(self, row_idx, new_status):
        """Обновляет статус фильма в базе данных"""
        title_item = self.favorite_table.item(row_idx, self.selected_columns.index("Название"))
        if title_item:
            movie_title = title_item.text()
            self.cursor.execute("UPDATE Movies SET Статус = ? WHERE Название = ?", (new_status, movie_title))
            self.conn.commit()  # Применяем изменения в базе данных
            self.main_window.update_table()  # Обновляем таблицу на главном окне
            self.main_window.updateButton()  # Обновляем кнопки на главном окне

    def update_favorite_status(self, item):
        """Обновляет статус 'Избранных' фильма в базе данных"""
        row = item.row()
        col = item.column()
        if col == self.selected_columns.index("Избранные"):  # Проверяем, что обновляется колонка "Избранные"
            movie_title = self.favorite_table.item(row, self.selected_columns.index("Название")).text()
            is_favorite = item.checkState() == Qt.CheckState.Checked  # Получаем новое состояние чекбокса
            self.cursor.execute("UPDATE Movies SET Избранные = ? WHERE Название = ?", (is_favorite, movie_title))
            self.conn.commit()  # Применяем изменения в базе данных
            self.main_window.update_table()  # Обновляем таблицу на главном окне
            if not is_favorite:
                self.favorite_table.removeRow(row)  # Удаляем строку, если фильм больше не в избранных

    def apply_theme(self):
        """Применяет тему оформления из главного окна"""
        self.setStyleSheet(self.main_window.styleSheet())


class ScoreWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        f_score = io.StringIO(score_pyqt)  # Загрузка UI из строки
        uic.loadUi(f_score, self)
        self.apply_theme()
        self.update_table()  # Обновляем таблицу сразу при запуске окна

    def update_table(self):
        self.cursor = self.main_window.cursor
        self.conn = self.main_window.conn

        # Указываем только нужные столбцы
        self.selected_columns = ["Название", "Жанр", "Режиссер", "Статус", "Избранные"]
        # Запрашиваем фильмы с оценкой 0 и статусом "Просмотрено"
        self.cursor.execute(f"SELECT {', '.join(self.selected_columns)} FROM Movies WHERE Оценка = 0 AND Статус = 'Просмотрено'")
        rows = self.cursor.fetchall()

        self.score_table.setRowCount(len(rows))  # Устанавливаем количество строк
        self.score_table.setColumnCount(len(self.selected_columns))  # Устанавливаем количество столбцов
        self.score_table.setHorizontalHeaderLabels(self.selected_columns)  # Заголовки столбцов

        # Заполняем таблицу данными
        for row_idx, row_data in enumerate(rows):
            for col_idx, value in enumerate(row_data):
                column_name = self.selected_columns[col_idx]
                if column_name == "Статус":
                    # Для "Статус" создаём выпадающий список
                    combo_box = QComboBox(self)
                    combo_box.addItems(["Не просмотрено", "В процессе", "Просмотрено"])
                    combo_box.setCurrentText(str(value))  # Устанавливаем текущий статус
                    combo_box.currentTextChanged.connect(
                        lambda new_status, r=row_idx: self.update_status(r, new_status)
                    )
                    self.score_table.setCellWidget(row_idx, col_idx, combo_box)

                elif column_name == "Избранные":
                    # Для "Избранных" создаём чекбокс
                    favorite_checkbox = QTableWidgetItem()
                    favorite_checkbox.setCheckState(Qt.CheckState.Checked if value else Qt.CheckState.Unchecked)
                    favorite_checkbox.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                    self.score_table.setItem(row_idx, col_idx, favorite_checkbox)

                else:
                    # Для других столбцов создаём обычный QTableWidgetItem
                    item = QTableWidgetItem(str(value))
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Ячейки не редактируемые
                    self.score_table.setItem(row_idx, col_idx, item)

        # Настройки отображения таблицы
        self.score_table.horizontalHeader().setStretchLastSection(True)  # Растягиваем последний столбец
        self.score_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)  # Автоматически растягиваем столбцы
        self.score_table.resizeColumnsToContents()  # Автоматически подбираем ширину столбцов
        self.score_table.resizeRowsToContents()  # Автоматически подбираем высоту строк

        self.score_table.itemChanged.connect(self.update_favorite_status)  # Обработчик изменений в чекбоксах
        self.score_table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)  # Отключаем возможность выделения строк
        self.score_table.doubleClicked.connect(
            lambda index: self.main_window.open_redactor_window(self, index, self.score_table)  # Открытие редактора по двойному клику
        )

    def update_status(self, row_idx, new_status):
        """Обновляет статус фильма в базе данных"""
        title_item = self.score_table.item(row_idx, self.selected_columns.index("Название"))
        if title_item:
            movie_title = title_item.text()
            self.cursor.execute("UPDATE Movies SET Статус = ? WHERE Название = ?", (new_status, movie_title))
            self.conn.commit()
            self.main_window.update_table()  # Обновляем таблицу на главном окне
            self.main_window.updateButton()  # Обновляем кнопки на главном окне

    def update_favorite_status(self, item):
        row = item.row()
        col = item.column()
        if col == self.selected_columns.index("Избранные"):  # Проверяем, что обновляется колонка "Избранные"
            movie_title = self.score_table.item(row, self.selected_columns.index("Название")).text()
            is_favorite = item.checkState() == Qt.CheckState.Checked
            self.cursor.execute("UPDATE Movies SET Избранные = ? WHERE Название = ?", (is_favorite, movie_title))
            self.conn.commit()
            self.main_window.update_table()  # Обновляем таблицу на главном окне

    def apply_theme(self):
        self.setStyleSheet(self.main_window.styleSheet())  # Применяем тему


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
