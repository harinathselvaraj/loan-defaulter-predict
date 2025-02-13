import json
from flask import Flask, render_template, send_file, request, jsonify
from requests import put, get
from flask_restful import reqparse

#ML
import numpy as np
import pandas as pd
import lightgbm as lgb

# EB looks for an 'application' callable by default.
application = Flask(__name__)

@application.route('/')
def default():
    return render_template("index.html")

# Define parser and request args
parser = reqparse.RequestParser()
parser.add_argument('var_0', type=float)
parser.add_argument('var_1', type=float)
parser.add_argument('var_2', type=float)
parser.add_argument('var_3', type=float)
parser.add_argument('var_4', type=float)
parser.add_argument('var_5', type=float)
parser.add_argument('var_6', type=float)
parser.add_argument('var_7', type=float)
parser.add_argument('var_8', type=float)
parser.add_argument('var_9', type=float)
parser.add_argument('var_10', type=float)
parser.add_argument('var_11', type=float)
parser.add_argument('var_12', type=float)
parser.add_argument('var_13', type=float)
parser.add_argument('var_14', type=float)
parser.add_argument('var_15', type=float)
parser.add_argument('var_16', type=float)
parser.add_argument('var_17', type=float)
parser.add_argument('var_18', type=float)
parser.add_argument('var_19', type=float)
parser.add_argument('var_20', type=float)
parser.add_argument('var_21', type=float)
parser.add_argument('var_22', type=float)
parser.add_argument('var_23', type=float)
parser.add_argument('var_24', type=float)
parser.add_argument('var_25', type=float)
parser.add_argument('var_26', type=float)
parser.add_argument('var_27', type=float)
parser.add_argument('var_28', type=float)
parser.add_argument('var_29', type=float)
parser.add_argument('var_30', type=float)
parser.add_argument('var_31', type=float)
parser.add_argument('var_32', type=float)
parser.add_argument('var_33', type=float)
parser.add_argument('var_34', type=float)
parser.add_argument('var_35', type=float)
parser.add_argument('var_36', type=float)
parser.add_argument('var_37', type=float)
parser.add_argument('var_38', type=float)
parser.add_argument('var_39', type=float)
parser.add_argument('var_40', type=float)
parser.add_argument('var_41', type=float)
parser.add_argument('var_42', type=float)
parser.add_argument('var_43', type=float)
parser.add_argument('var_44', type=float)
parser.add_argument('var_45', type=float)
parser.add_argument('var_46', type=float)
parser.add_argument('var_47', type=float)
parser.add_argument('var_48', type=float)
parser.add_argument('var_49', type=float)
parser.add_argument('var_50', type=float)
parser.add_argument('var_51', type=float)
parser.add_argument('var_52', type=float)
parser.add_argument('var_53', type=float)
parser.add_argument('var_54', type=float)
parser.add_argument('var_55', type=float)
parser.add_argument('var_56', type=float)
parser.add_argument('var_57', type=float)
parser.add_argument('var_58', type=float)
parser.add_argument('var_59', type=float)
parser.add_argument('var_60', type=float)
parser.add_argument('var_61', type=float)
parser.add_argument('var_62', type=float)
parser.add_argument('var_63', type=float)
parser.add_argument('var_64', type=float)
parser.add_argument('var_65', type=float)
parser.add_argument('var_66', type=float)
parser.add_argument('var_67', type=float)
parser.add_argument('var_68', type=float)
parser.add_argument('var_69', type=float)
parser.add_argument('var_70', type=float)
parser.add_argument('var_71', type=float)
parser.add_argument('var_72', type=float)
parser.add_argument('var_73', type=float)
parser.add_argument('var_74', type=float)
parser.add_argument('var_75', type=float)
parser.add_argument('var_76', type=float)
parser.add_argument('var_77', type=float)
parser.add_argument('var_78', type=float)
parser.add_argument('var_79', type=float)
parser.add_argument('var_80', type=float)
parser.add_argument('var_81', type=float)
parser.add_argument('var_82', type=float)
parser.add_argument('var_83', type=float)
parser.add_argument('var_84', type=float)
parser.add_argument('var_85', type=float)
parser.add_argument('var_86', type=float)
parser.add_argument('var_87', type=float)
parser.add_argument('var_88', type=float)
parser.add_argument('var_89', type=float)
parser.add_argument('var_90', type=float)
parser.add_argument('var_91', type=float)
parser.add_argument('var_92', type=float)
parser.add_argument('var_93', type=float)
parser.add_argument('var_94', type=float)
parser.add_argument('var_95', type=float)
parser.add_argument('var_96', type=float)
parser.add_argument('var_97', type=float)
parser.add_argument('var_98', type=float)
parser.add_argument('var_99', type=float)
parser.add_argument('var_100', type=float)
parser.add_argument('var_101', type=float)
parser.add_argument('var_102', type=float)
parser.add_argument('var_103', type=float)
parser.add_argument('var_104', type=float)
parser.add_argument('var_105', type=float)
parser.add_argument('var_106', type=float)
parser.add_argument('var_107', type=float)
parser.add_argument('var_108', type=float)
parser.add_argument('var_109', type=float)
parser.add_argument('var_110', type=float)
parser.add_argument('var_111', type=float)
parser.add_argument('var_112', type=float)
parser.add_argument('var_113', type=float)
parser.add_argument('var_114', type=float)
parser.add_argument('var_115', type=float)
parser.add_argument('var_116', type=float)
parser.add_argument('var_117', type=float)
parser.add_argument('var_118', type=float)
parser.add_argument('var_119', type=float)
parser.add_argument('var_120', type=float)
parser.add_argument('var_121', type=float)
parser.add_argument('var_122', type=float)
parser.add_argument('var_123', type=float)
parser.add_argument('var_124', type=float)
parser.add_argument('var_125', type=float)
parser.add_argument('var_126', type=float)
parser.add_argument('var_127', type=float)
parser.add_argument('var_128', type=float)
parser.add_argument('var_129', type=float)
parser.add_argument('var_130', type=float)
parser.add_argument('var_131', type=float)
parser.add_argument('var_132', type=float)
parser.add_argument('var_133', type=float)
parser.add_argument('var_134', type=float)
parser.add_argument('var_135', type=float)
parser.add_argument('var_136', type=float)
parser.add_argument('var_137', type=float)
parser.add_argument('var_138', type=float)
parser.add_argument('var_139', type=float)
parser.add_argument('var_140', type=float)
parser.add_argument('var_141', type=float)
parser.add_argument('var_142', type=float)
parser.add_argument('var_143', type=float)
parser.add_argument('var_144', type=float)
parser.add_argument('var_145', type=float)
parser.add_argument('var_146', type=float)
parser.add_argument('var_147', type=float)
parser.add_argument('var_148', type=float)
parser.add_argument('var_149', type=float)
parser.add_argument('var_150', type=float)
parser.add_argument('var_151', type=float)
parser.add_argument('var_152', type=float)
parser.add_argument('var_153', type=float)
parser.add_argument('var_154', type=float)
parser.add_argument('var_155', type=float)
parser.add_argument('var_156', type=float)
parser.add_argument('var_157', type=float)
parser.add_argument('var_158', type=float)
parser.add_argument('var_159', type=float)
parser.add_argument('var_160', type=float)
parser.add_argument('var_161', type=float)
parser.add_argument('var_162', type=float)
parser.add_argument('var_163', type=float)
parser.add_argument('var_164', type=float)
parser.add_argument('var_165', type=float)
parser.add_argument('var_166', type=float)
parser.add_argument('var_167', type=float)
parser.add_argument('var_168', type=float)
parser.add_argument('var_169', type=float)
parser.add_argument('var_170', type=float)
parser.add_argument('var_171', type=float)
parser.add_argument('var_172', type=float)
parser.add_argument('var_173', type=float)
parser.add_argument('var_174', type=float)
parser.add_argument('var_175', type=float)
parser.add_argument('var_176', type=float)
parser.add_argument('var_177', type=float)
parser.add_argument('var_178', type=float)
parser.add_argument('var_179', type=float)
parser.add_argument('var_180', type=float)
parser.add_argument('var_181', type=float)
parser.add_argument('var_182', type=float)
parser.add_argument('var_183', type=float)
parser.add_argument('var_184', type=float)
parser.add_argument('var_185', type=float)
parser.add_argument('var_186', type=float)
parser.add_argument('var_187', type=float)
parser.add_argument('var_188', type=float)
parser.add_argument('var_189', type=float)
parser.add_argument('var_190', type=float)
parser.add_argument('var_191', type=float)
parser.add_argument('var_192', type=float)
parser.add_argument('var_193', type=float)
parser.add_argument('var_194', type=float)
parser.add_argument('var_195', type=float)
parser.add_argument('var_196', type=float)
parser.add_argument('var_197', type=float)
parser.add_argument('var_198', type=float)
parser.add_argument('var_199', type=float)

@application.route('/api/', methods=['GET'])
def get():
    args =  request.args
    var_0 = float(args['var_0'])
    var_1 = float(args['var_1'])
    var_2 = float(args['var_2'])
    var_3 = float(args['var_3'])
    var_4 = float(args['var_4'])
    var_5 = float(args['var_5'])
    var_6 = float(args['var_6'])
    var_7 = float(args['var_7'])
    var_8 = float(args['var_8'])
    var_9 = float(args['var_9'])
    var_10 = float(args['var_10'])
    var_11 = float(args['var_11'])
    var_12 = float(args['var_12'])
    var_13 = float(args['var_13'])
    var_14 = float(args['var_14'])
    var_15 = float(args['var_15'])
    var_16 = float(args['var_16'])
    var_17 = float(args['var_17'])
    var_18 = float(args['var_18'])
    var_19 = float(args['var_19'])
    var_20 = float(args['var_20'])
    var_21 = float(args['var_21'])
    var_22 = float(args['var_22'])
    var_23 = float(args['var_23'])
    var_24 = float(args['var_24'])
    var_25 = float(args['var_25'])
    var_26 = float(args['var_26'])
    var_27 = float(args['var_27'])
    var_28 = float(args['var_28'])
    var_29 = float(args['var_29'])
    var_30 = float(args['var_30'])
    var_31 = float(args['var_31'])
    var_32 = float(args['var_32'])
    var_33 = float(args['var_33'])
    var_34 = float(args['var_34'])
    var_35 = float(args['var_35'])
    var_36 = float(args['var_36'])
    var_37 = float(args['var_37'])
    var_38 = float(args['var_38'])
    var_39 = float(args['var_39'])
    var_40 = float(args['var_40'])
    var_41 = float(args['var_41'])
    var_42 = float(args['var_42'])
    var_43 = float(args['var_43'])
    var_44 = float(args['var_44'])
    var_45 = float(args['var_45'])
    var_46 = float(args['var_46'])
    var_47 = float(args['var_47'])
    var_48 = float(args['var_48'])
    var_49 = float(args['var_49'])
    var_50 = float(args['var_50'])
    var_51 = float(args['var_51'])
    var_52 = float(args['var_52'])
    var_53 = float(args['var_53'])
    var_54 = float(args['var_54'])
    var_55 = float(args['var_55'])
    var_56 = float(args['var_56'])
    var_57 = float(args['var_57'])
    var_58 = float(args['var_58'])
    var_59 = float(args['var_59'])
    var_60 = float(args['var_60'])
    var_61 = float(args['var_61'])
    var_62 = float(args['var_62'])
    var_63 = float(args['var_63'])
    var_64 = float(args['var_64'])
    var_65 = float(args['var_65'])
    var_66 = float(args['var_66'])
    var_67 = float(args['var_67'])
    var_68 = float(args['var_68'])
    var_69 = float(args['var_69'])
    var_70 = float(args['var_70'])
    var_71 = float(args['var_71'])
    var_72 = float(args['var_72'])
    var_73 = float(args['var_73'])
    var_74 = float(args['var_74'])
    var_75 = float(args['var_75'])
    var_76 = float(args['var_76'])
    var_77 = float(args['var_77'])
    var_78 = float(args['var_78'])
    var_79 = float(args['var_79'])
    var_80 = float(args['var_80'])
    var_81 = float(args['var_81'])
    var_82 = float(args['var_82'])
    var_83 = float(args['var_83'])
    var_84 = float(args['var_84'])
    var_85 = float(args['var_85'])
    var_86 = float(args['var_86'])
    var_87 = float(args['var_87'])
    var_88 = float(args['var_88'])
    var_89 = float(args['var_89'])
    var_90 = float(args['var_90'])
    var_91 = float(args['var_91'])
    var_92 = float(args['var_92'])
    var_93 = float(args['var_93'])
    var_94 = float(args['var_94'])
    var_95 = float(args['var_95'])
    var_96 = float(args['var_96'])
    var_97 = float(args['var_97'])
    var_98 = float(args['var_98'])
    var_99 = float(args['var_99'])
    var_100 = float(args['var_100'])
    var_101 = float(args['var_101'])
    var_102 = float(args['var_102'])
    var_103 = float(args['var_103'])
    var_104 = float(args['var_104'])
    var_105 = float(args['var_105'])
    var_106 = float(args['var_106'])
    var_107 = float(args['var_107'])
    var_108 = float(args['var_108'])
    var_109 = float(args['var_109'])
    var_110 = float(args['var_110'])
    var_111 = float(args['var_111'])
    var_112 = float(args['var_112'])
    var_113 = float(args['var_113'])
    var_114 = float(args['var_114'])
    var_115 = float(args['var_115'])
    var_116 = float(args['var_116'])
    var_117 = float(args['var_117'])
    var_118 = float(args['var_118'])
    var_119 = float(args['var_119'])
    var_120 = float(args['var_120'])
    var_121 = float(args['var_121'])
    var_122 = float(args['var_122'])
    var_123 = float(args['var_123'])
    var_124 = float(args['var_124'])
    var_125 = float(args['var_125'])
    var_126 = float(args['var_126'])
    var_127 = float(args['var_127'])
    var_128 = float(args['var_128'])
    var_129 = float(args['var_129'])
    var_130 = float(args['var_130'])
    var_131 = float(args['var_131'])
    var_132 = float(args['var_132'])
    var_133 = float(args['var_133'])
    var_134 = float(args['var_134'])
    var_135 = float(args['var_135'])
    var_136 = float(args['var_136'])
    var_137 = float(args['var_137'])
    var_138 = float(args['var_138'])
    var_139 = float(args['var_139'])
    var_140 = float(args['var_140'])
    var_141 = float(args['var_141'])
    var_142 = float(args['var_142'])
    var_143 = float(args['var_143'])
    var_144 = float(args['var_144'])
    var_145 = float(args['var_145'])
    var_146 = float(args['var_146'])
    var_147 = float(args['var_147'])
    var_148 = float(args['var_148'])
    var_149 = float(args['var_149'])
    var_150 = float(args['var_150'])
    var_151 = float(args['var_151'])
    var_152 = float(args['var_152'])
    var_153 = float(args['var_153'])
    var_154 = float(args['var_154'])
    var_155 = float(args['var_155'])
    var_156 = float(args['var_156'])
    var_157 = float(args['var_157'])
    var_158 = float(args['var_158'])
    var_159 = float(args['var_159'])
    var_160 = float(args['var_160'])
    var_161 = float(args['var_161'])
    var_162 = float(args['var_162'])
    var_163 = float(args['var_163'])
    var_164 = float(args['var_164'])
    var_165 = float(args['var_165'])
    var_166 = float(args['var_166'])
    var_167 = float(args['var_167'])
    var_168 = float(args['var_168'])
    var_169 = float(args['var_169'])
    var_170 = float(args['var_170'])
    var_171 = float(args['var_171'])
    var_172 = float(args['var_172'])
    var_173 = float(args['var_173'])
    var_174 = float(args['var_174'])
    var_175 = float(args['var_175'])
    var_176 = float(args['var_176'])
    var_177 = float(args['var_177'])
    var_178 = float(args['var_178'])
    var_179 = float(args['var_179'])
    var_180 = float(args['var_180'])
    var_181 = float(args['var_181'])
    var_182 = float(args['var_182'])
    var_183 = float(args['var_183'])
    var_184 = float(args['var_184'])
    var_185 = float(args['var_185'])
    var_186 = float(args['var_186'])
    var_187 = float(args['var_187'])
    var_188 = float(args['var_188'])
    var_189 = float(args['var_189'])
    var_190 = float(args['var_190'])
    var_191 = float(args['var_191'])
    var_192 = float(args['var_192'])
    var_193 = float(args['var_193'])
    var_194 = float(args['var_194'])
    var_195 = float(args['var_195'])
    var_196 = float(args['var_196'])
    var_197 = float(args['var_197'])
    var_198 = float(args['var_198'])
    var_199 = float(args['var_199'])

    data = {'var_0' : var_0,'var_1' : var_1,'var_2' : var_2,'var_3' : var_3,'var_4' : var_4,'var_5' : var_5,'var_6' : var_6,'var_7' : var_7,'var_8' : var_8,'var_9' : var_9,'var_10' : var_10,'var_11' : var_11,'var_12' : var_12,'var_13' : var_13,'var_14' : var_14,'var_15' : var_15,'var_16' : var_16,'var_17' : var_17,'var_18' : var_18,'var_19' : var_19,'var_20' : var_20,'var_21' : var_21,'var_22' : var_22,'var_23' : var_23,'var_24' : var_24,'var_25' : var_25,'var_26' : var_26,'var_27' : var_27,'var_28' : var_28,'var_29' : var_29,'var_30' : var_30,'var_31' : var_31,'var_32' : var_32,'var_33' : var_33,'var_34' : var_34,'var_35' : var_35,'var_36' : var_36,'var_37' : var_37,'var_38' : var_38,'var_39' : var_39,'var_40' : var_40,'var_41' : var_41,'var_42' : var_42,'var_43' : var_43,'var_44' : var_44,'var_45' : var_45,'var_46' : var_46,'var_47' : var_47,'var_48' : var_48,'var_49' : var_49,'var_50' : var_50,'var_51' : var_51,'var_52' : var_52,'var_53' : var_53,'var_54' : var_54,'var_55' : var_55,'var_56' : var_56,'var_57' : var_57,'var_58' : var_58,'var_59' : var_59,'var_60' : var_60,'var_61' : var_61,'var_62' : var_62,'var_63' : var_63,'var_64' : var_64,'var_65' : var_65,'var_66' : var_66,'var_67' : var_67,'var_68' : var_68,'var_69' : var_69,'var_70' : var_70,'var_71' : var_71,'var_72' : var_72,'var_73' : var_73,'var_74' : var_74,'var_75' : var_75,'var_76' : var_76,'var_77' : var_77,'var_78' : var_78,'var_79' : var_79,'var_80' : var_80,'var_81' : var_81,'var_82' : var_82,'var_83' : var_83,'var_84' : var_84,'var_85' : var_85,'var_86' : var_86,'var_87' : var_87,'var_88' : var_88,'var_89' : var_89,'var_90' : var_90,'var_91' : var_91,'var_92' : var_92,'var_93' : var_93,'var_94' : var_94,'var_95' : var_95,'var_96' : var_96,'var_97' : var_97,'var_98' : var_98,'var_99' : var_99,'var_100' : var_100,'var_101' : var_101,'var_102' : var_102,'var_103' : var_103,'var_104' : var_104,'var_105' : var_105,'var_106' : var_106,'var_107' : var_107,'var_108' : var_108,'var_109' : var_109,'var_110' : var_110,'var_111' : var_111,'var_112' : var_112,'var_113' : var_113,'var_114' : var_114,'var_115' : var_115,'var_116' : var_116,'var_117' : var_117,'var_118' : var_118,'var_119' : var_119,'var_120' : var_120,'var_121' : var_121,'var_122' : var_122,'var_123' : var_123,'var_124' : var_124,'var_125' : var_125,'var_126' : var_126,'var_127' : var_127,'var_128' : var_128,'var_129' : var_129,'var_130' : var_130,'var_131' : var_131,'var_132' : var_132,'var_133' : var_133,'var_134' : var_134,'var_135' : var_135,'var_136' : var_136,'var_137' : var_137,'var_138' : var_138,'var_139' : var_139,'var_140' : var_140,'var_141' : var_141,'var_142' : var_142,'var_143' : var_143,'var_144' : var_144,'var_145' : var_145,'var_146' : var_146,'var_147' : var_147,'var_148' : var_148,'var_149' : var_149,'var_150' : var_150,'var_151' : var_151,'var_152' : var_152,'var_153' : var_153,'var_154' : var_154,'var_155' : var_155,'var_156' : var_156,'var_157' : var_157,'var_158' : var_158,'var_159' : var_159,'var_160' : var_160,'var_161' : var_161,'var_162' : var_162,'var_163' : var_163,'var_164' : var_164,'var_165' : var_165,'var_166' : var_166,'var_167' : var_167,'var_168' : var_168,'var_169' : var_169,'var_170' : var_170,'var_171' : var_171,'var_172' : var_172,'var_173' : var_173,'var_174' : var_174,'var_175' : var_175,'var_176' : var_176,'var_177' : var_177,'var_178' : var_178,'var_179' : var_179,'var_180' : var_180,'var_181' : var_181,'var_182' : var_182,'var_183' : var_183,'var_184' : var_184,'var_185' : var_185,'var_186' : var_186,'var_187' : var_187,'var_188' : var_188,'var_189' : var_189,'var_190' : var_190,'var_191' : var_191,'var_192' : var_192,'var_193' : var_193,'var_194' : var_194,'var_195' : var_195,'var_196' : var_196,'var_197' : var_197,'var_198' : var_198,'var_199' : var_199}
    x_test = pd.DataFrame(data,columns=data.keys(), index=[0])
    model = lgb.Booster(model_file="model/lightGBM_model.txt")
    y_pred = model.predict(x_test)
    return str(y_pred[0])

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()