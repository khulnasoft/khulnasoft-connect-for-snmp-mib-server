#
# PySNMP MIB module ServersCheck (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ServersCheck
# Produced by pysmi-0.3.4 at Mon Apr 29 21:07:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, ObjectIdentity, TimeTicks, enterprises, MibIdentifier, NotificationType, Counter64, Gauge32, IpAddress, Bits, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "ObjectIdentity", "TimeTicks", "enterprises", "MibIdentifier", "NotificationType", "Counter64", "Gauge32", "IpAddress", "Bits", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
serverscheck = MibIdentifier((1, 3, 6, 1, 4, 1, 17095))
product = MibIdentifier((1, 3, 6, 1, 4, 1, 17095, 1))
productname = MibScalar((1, 3, 6, 1, 4, 1, 17095, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productname.setStatus('mandatory')
productversion = MibScalar((1, 3, 6, 1, 4, 1, 17095, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productversion.setStatus('mandatory')
productdate = MibScalar((1, 3, 6, 1, 4, 1, 17095, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productdate.setStatus('mandatory')
productusername = MibScalar((1, 3, 6, 1, 4, 1, 17095, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productusername.setStatus('mandatory')
productuserloc = MibScalar((1, 3, 6, 1, 4, 1, 17095, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productuserloc.setStatus('mandatory')
productnetip = MibScalar((1, 3, 6, 1, 4, 1, 17095, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productnetip.setStatus('mandatory')
productnetgateway = MibScalar((1, 3, 6, 1, 4, 1, 17095, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productnetgateway.setStatus('mandatory')
productnetpridns = MibScalar((1, 3, 6, 1, 4, 1, 17095, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productnetpridns.setStatus('mandatory')
productnetsecdns = MibScalar((1, 3, 6, 1, 4, 1, 17095, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productnetsecdns.setStatus('mandatory')
setup = MibIdentifier((1, 3, 6, 1, 4, 1, 17095, 2))
traps = MibTable((1, 3, 6, 1, 4, 1, 17095, 2, 1), )
if mibBuilder.loadTexts: traps.setStatus('mandatory')
trapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 17095, 2, 1, 1), ).setIndexNames((0, "ServersCheck", "trapReceiverNumber"))
if mibBuilder.loadTexts: trapEntry.setStatus('mandatory')
trapReceiverNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 17095, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3)))
if mibBuilder.loadTexts: trapReceiverNumber.setStatus('mandatory')
trapEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 17095, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapEnabled.setStatus('mandatory')
trapReceiverIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 17095, 2, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapReceiverIPAddress.setStatus('mandatory')
trapCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 17095, 2, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapCommunity.setStatus('mandatory')
control = MibIdentifier((1, 3, 6, 1, 4, 1, 17095, 3))
sensor1name = MibScalar((1, 3, 6, 1, 4, 1, 17095, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor1name.setStatus('mandatory')
sensor1Value = MibScalar((1, 3, 6, 1, 4, 1, 17095, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor1Value.setStatus('mandatory')
sensor1LastErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor1LastErrMsg.setStatus('mandatory')
sensor1LastErrTime = MibScalar((1, 3, 6, 1, 4, 1, 17095, 3, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor1LastErrTime.setStatus('mandatory')
sensor2name = MibScalar((1, 3, 6, 1, 4, 1, 17095, 3, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor2name.setStatus('mandatory')
sensor2Value = MibScalar((1, 3, 6, 1, 4, 1, 17095, 3, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor2Value.setStatus('mandatory')
sensor2LastErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 3, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor2LastErrMsg.setStatus('mandatory')
sensor2LastErrTime = MibScalar((1, 3, 6, 1, 4, 1, 17095, 3, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor2LastErrTime.setStatus('mandatory')
sensor3name = MibScalar((1, 3, 6, 1, 4, 1, 17095, 3, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor3name.setStatus('mandatory')
sensor3Value = MibScalar((1, 3, 6, 1, 4, 1, 17095, 3, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor3Value.setStatus('mandatory')
sensor3LastErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 3, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor3LastErrMsg.setStatus('mandatory')
sensor3LastErrTime = MibScalar((1, 3, 6, 1, 4, 1, 17095, 3, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor3LastErrTime.setStatus('mandatory')
sensor4name = MibScalar((1, 3, 6, 1, 4, 1, 17095, 3, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor4name.setStatus('mandatory')
sensor4Value = MibScalar((1, 3, 6, 1, 4, 1, 17095, 3, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor4Value.setStatus('mandatory')
sensor4LastErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 3, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor4LastErrMsg.setStatus('mandatory')
sensor4LastErrTime = MibScalar((1, 3, 6, 1, 4, 1, 17095, 3, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor4LastErrTime.setStatus('mandatory')
sensor5name = MibScalar((1, 3, 6, 1, 4, 1, 17095, 3, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor5name.setStatus('mandatory')
sensor5Value = MibScalar((1, 3, 6, 1, 4, 1, 17095, 3, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor5Value.setStatus('mandatory')
sensor5LastErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 3, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor5LastErrMsg.setStatus('mandatory')
sensor5LastErrTime = MibScalar((1, 3, 6, 1, 4, 1, 17095, 3, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor5LastErrTime.setStatus('mandatory')
trapalerts = MibIdentifier((1, 3, 6, 1, 4, 1, 17095, 4))
sensor1TrapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 4, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor1TrapErrMsg.setStatus('mandatory')
sensor2TrapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 4, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor2TrapErrMsg.setStatus('mandatory')
sensor3TrapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 4, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor3TrapErrMsg.setStatus('mandatory')
sensor4TrapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 4, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor4TrapErrMsg.setStatus('mandatory')
sensor5TrapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 4, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor5TrapErrMsg.setStatus('mandatory')
sensor6TrapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 4, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor6TrapErrMsg.setStatus('mandatory')
sensorAlert = NotificationType((1, 3, 6, 1, 4, 1, 17095) + (0,1)).setObjects(("ServersCheck", "sensor1TrapErrMsg"), ("ServersCheck", "sensor2TrapErrMsg"), ("ServersCheck", "sensor3TrapErrMsg"), ("ServersCheck", "sensor4TrapErrMsg"), ("ServersCheck", "sensor5TrapErrMsg"), ("ServersCheck", "sensor6TrapErrMsg"))
iotrapalerts = MibIdentifier((1, 3, 6, 1, 4, 1, 17095, 5))
iosensorINPUT1trapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 5, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iosensorINPUT1trapErrMsg.setStatus('mandatory')
iosensorINPUT2trapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 5, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iosensorINPUT2trapErrMsg.setStatus('mandatory')
iosensorINPUT3trapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 5, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iosensorINPUT3trapErrMsg.setStatus('mandatory')
iosensorINPUT4trapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 5, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iosensorINPUT4trapErrMsg.setStatus('mandatory')
iosensorINPUT5trapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 5, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iosensorINPUT5trapErrMsg.setStatus('mandatory')
iosensorINPUT6trapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 5, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iosensorINPUT6trapErrMsg.setStatus('mandatory')
iosensorINPUT7trapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 5, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iosensorINPUT7trapErrMsg.setStatus('mandatory')
iosensorINPUT8trapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 5, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iosensorINPUT8trapErrMsg.setStatus('mandatory')
iosensorINPUT9trapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 5, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iosensorINPUT9trapErrMsg.setStatus('mandatory')
iosensorINPUT10trapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 5, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iosensorINPUT10trapErrMsg.setStatus('mandatory')
iosensorINPUT11trapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 5, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iosensorINPUT11trapErrMsg.setStatus('mandatory')
iosensorINPUT12trapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 5, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iosensorINPUT12trapErrMsg.setStatus('mandatory')
iosensorINPUT13trapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 5, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iosensorINPUT13trapErrMsg.setStatus('mandatory')
iosensorINPUT14trapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 5, 14), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iosensorINPUT14trapErrMsg.setStatus('mandatory')
iosensorINPUT15trapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 5, 15), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iosensorINPUT15trapErrMsg.setStatus('mandatory')
iosensorINPUT16trapErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 5, 16), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iosensorINPUT16trapErrMsg.setStatus('mandatory')
iosensorAlert = NotificationType((1, 3, 6, 1, 4, 1, 17095) + (0,0)).setObjects(("ServersCheck", "iosensorINPUT1trapErrMsg"), ("ServersCheck", "iosensorINPUT2trapErrMsg"), ("ServersCheck", "iosensorINPUT3trapErrMsg"), ("ServersCheck", "iosensorINPUT4trapErrMsg"), ("ServersCheck", "iosensorINPUT5trapErrMsg"), ("ServersCheck", "iosensorINPUT6trapErrMsg"), ("ServersCheck", "iosensorINPUT7trapErrMsg"), ("ServersCheck", "iosensorINPUT8trapErrMsg"), ("ServersCheck", "iosensorINPUT9trapErrMsg"), ("ServersCheck", "iosensorINPUT10trapErrMsg"), ("ServersCheck", "iosensorINPUT11trapErrMsg"), ("ServersCheck", "iosensorINPUT12trapErrMsg"), ("ServersCheck", "iosensorINPUT13trapErrMsg"), ("ServersCheck", "iosensorINPUT14trapErrMsg"), ("ServersCheck", "iosensorINPUT15trapErrMsg"), ("ServersCheck", "iosensorINPUT16trapErrMsg"))
input = MibIdentifier((1, 3, 6, 1, 4, 1, 17095, 6))
input1name = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input1name.setStatus('mandatory')
input1Value = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input1Value.setStatus('mandatory')
input1LastErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input1LastErrMsg.setStatus('mandatory')
input2name = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input2name.setStatus('mandatory')
input2Value = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input2Value.setStatus('mandatory')
input2LastErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input2LastErrMsg.setStatus('mandatory')
input3name = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input3name.setStatus('mandatory')
input3Value = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input3Value.setStatus('mandatory')
input3LastErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input3LastErrMsg.setStatus('mandatory')
input4name = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input4name.setStatus('mandatory')
input4Value = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input4Value.setStatus('mandatory')
input4LastErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input4LastErrMsg.setStatus('mandatory')
input5name = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input5name.setStatus('mandatory')
input5Value = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input5Value.setStatus('mandatory')
input5LastErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input5LastErrMsg.setStatus('mandatory')
input6name = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input6name.setStatus('mandatory')
input6Value = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input6Value.setStatus('mandatory')
input6LastErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input6LastErrMsg.setStatus('mandatory')
input7name = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input7name.setStatus('mandatory')
input7Value = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input7Value.setStatus('mandatory')
input7LastErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 21), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input7LastErrMsg.setStatus('mandatory')
input8name = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 22), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input8name.setStatus('mandatory')
input8Value = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 23), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input8Value.setStatus('mandatory')
input8LastErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 24), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input8LastErrMsg.setStatus('mandatory')
input9name = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 25), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input9name.setStatus('mandatory')
input9Value = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 26), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input9Value.setStatus('mandatory')
input9LastErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 27), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input9LastErrMsg.setStatus('mandatory')
input10name = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 28), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input10name.setStatus('mandatory')
input10Value = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 29), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input10Value.setStatus('mandatory')
input10LastErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 30), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input10LastErrMsg.setStatus('mandatory')
input11name = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 31), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input11name.setStatus('mandatory')
input11Value = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 32), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input11Value.setStatus('mandatory')
input11LastErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 33), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input11LastErrMsg.setStatus('mandatory')
input12name = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 34), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input12name.setStatus('mandatory')
input12Value = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 35), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input12Value.setStatus('mandatory')
input12LastErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 36), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input12LastErrMsg.setStatus('mandatory')
input13name = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 37), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input13name.setStatus('mandatory')
input13Value = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 38), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input13Value.setStatus('mandatory')
input13LastErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 39), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input13LastErrMsg.setStatus('mandatory')
input14name = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 40), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input14name.setStatus('mandatory')
input14Value = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 41), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input14Value.setStatus('mandatory')
input14LastErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 42), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input14LastErrMsg.setStatus('mandatory')
input15name = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 43), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input15name.setStatus('mandatory')
input15Value = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 44), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input15Value.setStatus('mandatory')
input15LastErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 45), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input15LastErrMsg.setStatus('mandatory')
input16name = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 46), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input16name.setStatus('mandatory')
input16Value = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 47), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input16Value.setStatus('mandatory')
input16LastErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 17095, 6, 48), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: input16LastErrMsg.setStatus('mandatory')
output = MibIdentifier((1, 3, 6, 1, 4, 1, 17095, 7))
output1State = MibScalar((1, 3, 6, 1, 4, 1, 17095, 7, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: output1State.setStatus('mandatory')
output2State = MibScalar((1, 3, 6, 1, 4, 1, 17095, 7, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: output2State.setStatus('mandatory')
output3State = MibScalar((1, 3, 6, 1, 4, 1, 17095, 7, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: output3State.setStatus('mandatory')
output4State = MibScalar((1, 3, 6, 1, 4, 1, 17095, 7, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: output4State.setStatus('mandatory')
mibBuilder.exportSymbols("ServersCheck", iosensorINPUT15trapErrMsg=iosensorINPUT15trapErrMsg, input=input, sensor4TrapErrMsg=sensor4TrapErrMsg, sensor4name=sensor4name, traps=traps, input10Value=input10Value, input2Value=input2Value, input3name=input3name, input11Value=input11Value, sensor5LastErrTime=sensor5LastErrTime, iosensorINPUT6trapErrMsg=iosensorINPUT6trapErrMsg, input12name=input12name, sensor1Value=sensor1Value, iosensorINPUT11trapErrMsg=iosensorINPUT11trapErrMsg, input15LastErrMsg=input15LastErrMsg, sensor1LastErrMsg=sensor1LastErrMsg, iotrapalerts=iotrapalerts, sensor5Value=sensor5Value, input16Value=input16Value, input13LastErrMsg=input13LastErrMsg, trapReceiverNumber=trapReceiverNumber, sensor2Value=sensor2Value, sensor2name=sensor2name, input3LastErrMsg=input3LastErrMsg, productuserloc=productuserloc, input13Value=input13Value, trapCommunity=trapCommunity, input16name=input16name, iosensorINPUT16trapErrMsg=iosensorINPUT16trapErrMsg, sensor5name=sensor5name, sensor3TrapErrMsg=sensor3TrapErrMsg, productnetgateway=productnetgateway, input11name=input11name, productversion=productversion, sensor3Value=sensor3Value, sensor3LastErrTime=sensor3LastErrTime, trapalerts=trapalerts, input2name=input2name, input9name=input9name, input1name=input1name, input10LastErrMsg=input10LastErrMsg, input8name=input8name, sensor2LastErrTime=sensor2LastErrTime, output4State=output4State, input4Value=input4Value, input2LastErrMsg=input2LastErrMsg, productdate=productdate, sensor4LastErrMsg=sensor4LastErrMsg, iosensorINPUT8trapErrMsg=iosensorINPUT8trapErrMsg, input12Value=input12Value, control=control, trapReceiverIPAddress=trapReceiverIPAddress, sensor6TrapErrMsg=sensor6TrapErrMsg, iosensorINPUT14trapErrMsg=iosensorINPUT14trapErrMsg, iosensorINPUT9trapErrMsg=iosensorINPUT9trapErrMsg, iosensorINPUT10trapErrMsg=iosensorINPUT10trapErrMsg, productusername=productusername, input7LastErrMsg=input7LastErrMsg, iosensorAlert=iosensorAlert, input5LastErrMsg=input5LastErrMsg, sensor1TrapErrMsg=sensor1TrapErrMsg, output1State=output1State, trapEntry=trapEntry, productname=productname, iosensorINPUT5trapErrMsg=iosensorINPUT5trapErrMsg, input9LastErrMsg=input9LastErrMsg, input3Value=input3Value, input6LastErrMsg=input6LastErrMsg, trapEnabled=trapEnabled, sensorAlert=sensorAlert, sensor4LastErrTime=sensor4LastErrTime, input10name=input10name, input5Value=input5Value, input9Value=input9Value, sensor3name=sensor3name, input15Value=input15Value, sensor2TrapErrMsg=sensor2TrapErrMsg, input6Value=input6Value, input12LastErrMsg=input12LastErrMsg, iosensorINPUT1trapErrMsg=iosensorINPUT1trapErrMsg, productnetpridns=productnetpridns, input8Value=input8Value, input4LastErrMsg=input4LastErrMsg, input13name=input13name, input16LastErrMsg=input16LastErrMsg, iosensorINPUT4trapErrMsg=iosensorINPUT4trapErrMsg, productnetsecdns=productnetsecdns, input1LastErrMsg=input1LastErrMsg, output2State=output2State, input14Value=input14Value, serverscheck=serverscheck, sensor1name=sensor1name, input11LastErrMsg=input11LastErrMsg, input7name=input7name, input7Value=input7Value, sensor4Value=sensor4Value, iosensorINPUT13trapErrMsg=iosensorINPUT13trapErrMsg, input1Value=input1Value, iosensorINPUT3trapErrMsg=iosensorINPUT3trapErrMsg, iosensorINPUT2trapErrMsg=iosensorINPUT2trapErrMsg, sensor2LastErrMsg=sensor2LastErrMsg, sensor5TrapErrMsg=sensor5TrapErrMsg, input8LastErrMsg=input8LastErrMsg, input15name=input15name, sensor3LastErrMsg=sensor3LastErrMsg, output=output, productnetip=productnetip, setup=setup, sensor1LastErrTime=sensor1LastErrTime, input4name=input4name, iosensorINPUT7trapErrMsg=iosensorINPUT7trapErrMsg, output3State=output3State, iosensorINPUT12trapErrMsg=iosensorINPUT12trapErrMsg, input14name=input14name, input14LastErrMsg=input14LastErrMsg, sensor5LastErrMsg=sensor5LastErrMsg, input6name=input6name, input5name=input5name, product=product)
