#
# PySNMP MIB module T0510-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/T0510-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:07:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, IpAddress, Gauge32, TimeTicks, Counter64, Unsigned32, ObjectIdentity, enterprises, Counter32, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "IpAddress", "Gauge32", "TimeTicks", "Counter64", "Unsigned32", "ObjectIdentity", "enterprises", "Counter32", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

comet = MibIdentifier((1, 3, 6, 1, 4, 1, 22626))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1))
t0510 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2))
readings = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1))
settings = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2))
readingsint = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3))
settingsint = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 5))
tables = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6))
temperature = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature.setStatus('mandatory')
templow = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: templow.setStatus('mandatory')
temphigh = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temphigh.setStatus('mandatory')
temptime = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temptime.setStatus('mandatory')
tempHyst = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempHyst.setStatus('mandatory')
temperaturei = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperaturei.setStatus('mandatory')
templowi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: templowi.setStatus('mandatory')
temphighi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: temphighi.setStatus('mandatory')
humiditylowi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: humiditylowi.setStatus('mandatory')
temptimei = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: temptimei.setStatus('mandatory')
tempHysti = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tempHysti.setStatus('mandatory')
humidityHysti = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: humidityHysti.setStatus('mandatory')
messageString = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: messageString.setStatus('mandatory')
alarmTemperature = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmTemperature.setStatus('mandatory')
historyTable = MibTable((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1), )
if mibBuilder.loadTexts: historyTable.setStatus('mandatory')
historyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1), ).setIndexNames((0, "T0510-MIB", "histtemperature"))
if mibBuilder.loadTexts: historyEntry.setStatus('optional')
histtemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: histtemperature.setStatus('mandatory')
mibBuilder.exportSymbols("T0510-MIB", historyEntry=historyEntry, templow=templow, products=products, temperaturei=temperaturei, humiditylowi=humiditylowi, readingsint=readingsint, alarmTemperature=alarmTemperature, temphighi=temphighi, readings=readings, comet=comet, DisplayString=DisplayString, temptime=temptime, settings=settings, t0510=t0510, histtemperature=histtemperature, messageString=messageString, traps=traps, settingsint=settingsint, tables=tables, temperature=temperature, templowi=templowi, tempHyst=tempHyst, temphigh=temphigh, temptimei=temptimei, tempHysti=tempHysti, humidityHysti=humidityHysti, historyTable=historyTable)
