FUNCTIONS = (
    # arithmetic / logic
    'plus',
    'minus',
    'multiply',
    'divide',
    'intDiv',
    'intDivOrZero',
    'modulo',
    'negate',
    'abs',
    'bitAnd',
    'bitOr',
    'bitXor',
    'bitNot',
    'bitShiftLeft',
    'bitShiftRight',
    'equals',
    'notEquals',
    'less',
    'greater',
    'lessOrEquals',
    'greaterOrEquals',
    'and',
    'or',
    'not',
    'xor',

    # type conversion
    'toUInt8',
    'toUInt16',
    'toUInt32',
    'toUInt64',
    'toInt8',
    'toInt16',
    'toInt32',
    'toInt64',
    'toFloat32',
    'toFloat64',
    'toDate',
    'toDateTime',
    'toString',
    'toFixedString',
    'toStringCutToZero',

    'reinterpretAsUInt8',
    'reinterpretAsUInt16',
    'reinterpretAsUInt32',
    'reinterpretAsUInt64',
    'reinterpretAsInt8',
    'reinterpretAsInt16',
    'reinterpretAsInt32',
    'reinterpretAsInt64',
    'reinterpretAsFloat32',
    'reinterpretAsFloat64',
    'reinterpretAsDate',
    'reinterpretAsDateTime',
    'reinterpretAsString',

    # date/time

    'toYear',
    'toMonth',
    'toDayOfMonth',
    'toDayOfWeek',
    'toHour',
    'toMinute',
    'toSecond',
    'toMonday',
    'toStartOfMonth',
    'toStartOfQuarter',
    'toStartOfYear',
    'toStartOfMinute',
    'toStartOfFiveMinute',
    'toStartOfHour',
    'toTime',
    'toRelativeYearNum',
    'toRelativeMonthNum',
    'toRelativeWeekNum',
    'toRelativeDayNum',
    'toRelativeHourNum',
    'toRelativeMinuteNum',
    'toRelativeSecondNum',
    'now',
    'today',
    'yesterday',
    'timeSlot',
    'timeSlots',

    # string
    'empty',
    'notEmpty',
    'length',
    'lengthUTF8',
    'lower',
    'upper',
    'lowerUTF8',
    'upperUTF8',
    'reverse',
    'reverseUTF8',
    'concat',
    'substring',
    'substringUTF8',
    'appendTrailingCharIfAbsent',

    # string find
    'position',
    'positionUTF8',
    'match',
    'extract',
    'extractAll',
    'like',
    'notLike',

    # string find & replace
    'replaceOne',
    'replaceAll',
    'replaceRegexpOne',
    'replaceRegexpAll',

    # array
    'empty',
    'notEmpty',
    'length',
    'emptyArrayUInt8',
    'emptyArrayUInt16',
    'emptyArrayUInt32',
    'emptyArrayUInt64',
    'emptyArrayInt8',
    'emptyArrayInt16',
    'emptyArrayInt32',
    'emptyArrayInt64',
    'emptyArrayFloat32',
    'emptyArrayFloat64',
    'emptyArrayDate',
    'emptyArrayDateTime',
    'emptyArrayString',
    'range',
    'array',
    'arrayElement',
    'has',
    'indexOf',
    'countEqual',
    'arrayEnumerate',
    'arrayEnumerateUniq',
    'arrayJoin',

    # higher-level
    'lambda',
    'arrayMap',
    'arrayFilter',
    'arrayCount',
    'arrayExists',
    'arrayAll',
    'arraySum',
    'arrayFirst',
    'arrayFirstIndex',

    # array / string
    'splitByChar',
    'splitByString',
    'alphaTokens',

    # URL
    'protocol',
    'domain',
    'domainWithoutWWW',
    'topLevelDomain',
    'firstSignificantSubdomain',
    'cutToFirstSignificantSubdomain',
    'path',
    'pathFull',
    'queryString',
    'fragment',
    'queryStringAndFragment',
    'extractURLParameter',
    'extractURLParameters',
    'extractURLParameterNames',
    'URLHierarchy',
    'URLPathHierarchy',
    'cutWWW',
    'cutQueryString',
    'cutFragment',
    'cutQueryStringAndFragment',
    'cutURLParameter',

    # IP
    'IPv4NumToString',
    'IPv4StringToNum',
    'IPv4NumToStringClassC',
    'IPv6NumToString',
    'IPv6StringToNum',

    # PRNG
    'rand',
    'rand64',

    # hash
    'halfMD5',
    'MD5',
    'sipHash64',
    'sipHash128',
    'cityHash64',
    'intHash32',
    'intHash64',
    'SHA1',
    'SHA224',
    'SHA256',
    'URLHash',

    # encode / decode
    'hex',
    'unhex',
    'bitmaskToList',
    'bitmaskToArray',

    # rounding
    'floor',
    'ceil',
    'round',
    'roundToExp2',
    'roundDuration',
    'roundAge',

    # conditional
    'if',

    # math
    'e',
    'pi',
    'exp',
    'log',
    'exp2',
    'log2',
    'exp10',
    'log10',
    'sqrt',
    'cbrt',
    'erf',
    'erfc',
    'lgamma',
    'tgamma',
    'sin',
    'cos',
    'tan',
    'asin',
    'acos',
    'atan',
    'pow',

    # metrika dictionaries
    'regionToCity',
    'regionToArea',
    'regionToDistrict',
    'regionToCountry',
    'regionToContinent',
    'regionToPopulation',
    'regionIn',
    'regionHierarchy',
    'regionToName',
    'OSToRoot',
    'OSIn',
    'OSHierarchy',
    'SEToRoot',
    'SEIn',
    'SEHierarchy',

    # external dictionaries
    'dictGetUInt8',
    'dictGetUInt16',
    'dictGetUInt32',
    'dictGetUInt64',
    'dictGetInt8',
    'dictGetInt16',
    'dictGetInt32',
    'dictGetInt64',
    'dictGetFloat32',
    'dictGetFloat64',
    'dictGetDate',
    'dictGetDateTime',
    'dictGetString',
    'dictGetTOrDefault',
    'dictIsIn',
    'dictGetHierarchy',
    'dictHas',

    # json
    'visitParamHas',
    'visitParamExtractUInt',
    'visitParamExtractInt',
    'visitParamExtractFloat',
    'visitParamExtractBool',
    'visitParamExtractRaw',
    'visitParamExtractString',

    # IN support
    'in',
    'notIn',
    'globalIn',
    'globalNotIn',
    'tuple',
    'tupleElement',

    # misc
    'hostName',
    'visibleWidth',
    'toTypeName',
    'blockSize',
    'materialize',
    'ignore',
    'sleep',
    'currentDatabase',
    'isFinite',
    'isInfinite',
    'isNaN',
    'bar',
    'transform',

    'arrayJoin',
)

CASE_INSENSITIVE_FUNCTIONS = (
    'COUNT',

    'CORR',
    'VAR_SAMP',
    'VAR_POP',
    'STDDEV_SAMP',
    'STDDEV_POP',
    'COVAR_SAMP',
    'COVAR_POP',

    'AVG',
    'SUM',
    'MIN',
    'MAX',
)

AGGREGATION_FUNCTIONS = (
    'count',
    'any',
    'anyLast',
    'min',
    'max',
    'argMin',
    'argMax',
    'sum',
    'avg',
    'uniq',
    'uniqCombined',
    'uniqHLL12',
    'uniqExact',
    'groupArray',
    'groupUniqArray',
    'quantile',
    'quantileDeterministic',
    'quantileTiming',
    'quantileTimingWeighted',
    'quantileExact',
    'quantileExactWeighted',
    'quantileTDigest',
    'median',
    'quantiles',
    'varSamp',
    'varPop',
    'stddevSamp',
    'stddevPop',
    'covarSamp',
    'covarPop',
    'corr',
    'sequenceMatch',
    'sequenceCount',
    'uniqUpTo',
)

DATATYPES = (
    'UInt8',
    'UInt16',
    'UInt32',
    'UInt64',
    'Int8',
    'Int16',
    'Int32',
    'Int64',
    'Float32',
    'Float64',
    'String',
    'FixedString',
    'Date',
    'DateTime',
    'Enum',
    'Array',
    'Tuple',
    'Nested',
)

OPERATORS = (
    'LIKE',
    'NOT LIKE',
    'IN',
    'NOT IN',
    'GLOBAL IN',
    'GLOBAL NOT IN',
    'AND',
    'OR',
    'NOT'
)

FORMATS = [
    'Native',
    'TabSeparated',
    'TabSeparatedWithNames',
    'TabSeparatedWithNamesAndTypes',
    'TabSeparatedRaw',
    'BlockTabSeparated',
    'CSV',
    'CSVWithNames',
    'RowBinary',
    'Pretty',
    'PrettyCompact',
    'PrettyCompactMonoBlock',
    'PrettySpace',
    'PrettyNoEscapes',
    'PrettyCompactNoEscapes',
    'PrettySpaceNoEscapes',
    'Vertical',
    'Values',
    'JSON',
    'JSONCompact',
    'JSONEachRow',
    'TSKV',
    'XML',
    'Null',
]


READ_QUERIES = (
    'SELECT',
    'SHOW',
    'DESCRIBE',
    'USE',
)

WRITE_QUERIES = (
    'INSERT',
    'CREATE',
    'ATTACH',
    'DROP',
    'RENAME',
    'ALTER',
    'EXISTS',
    'SET',
    'OPTIMIZE',
)

FORMATTABLE_QUERIES = (
    'INSERT',
    'SELECT',
    'SHOW',
    'DESCRIBE',
    'EXISTS',
)

KEYWORDS = (
    'ADD',
    'AFTER',
    'ALIAS',
    'ALL',
    'AND',
    'ANY',
    'ARRAY',
    'AS',
    'ASC',
    'ATTACH',
    'BY',
    'COLUMN',
    'CREATE',
    'DATABASE',
    'DATABASES',
    'DEFAULT',
    'DELETE',
    'DESC',
    'DESCRIBE',
    'DETACH',
    'DISTINCT',
    'DROP',
    'ENGINE',
    'EXISTS',
    'FALSE',
    'FETCH',
    'FINAL',
    'FIRST',
    'FOR',
    'FORMAT',
    'FREEZE',
    'FROM',
    'GLOBAL',
    'GROUP',
    'HAVING',
    'IF',
    'IN',
    'INNER',
    'INSERT',
    'INTO',
    'IS',
    'JOIN',
    'LEFT',
    'LIKE',
    'LIMIT',
    'MATERIALIZED',
    'MODIFY',
    'NOT',
    'OF',
    'ON',
    'OPTIMIZE',
    'OR',
    'ORDER',
    'OUTER',
    'PARTITION',
    'POPULATE',
    'PREWHERE',
    'PROCESSLIST',
    'RENAME',
    'RIGHT',
    'SAMPLE',
    'SELECT',
    'SET',
    'SHOW',
    'TABLE',
    'TABLES',
    'TEMPORARY',
    'TO',
    'TOTALS',
    'UNION',
    'UNREPLICATED',
    'UPDATE',
    'USE',
    'USING',
    'VALUES',
    'VIEW',
    'WHERE',
    'WITH',
)

EXIT_COMMANDS = (
    'exit',
    'quit',
    'logout',
    'учше',
    'йгше',
    'дщпщге',
    'exit;',
    'quit;',
    'logout;',
    'учшеж',
    'йгшеж',
    'дщпщгеж',
    'q',
    'й',
    '\q',
    '\Q',
    ':q',
    '\й',
    '\Й',
    'Жй',
)

INTERNAL_COMMANDS = (
    'help',
) + EXIT_COMMANDS
