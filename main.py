from bs4 import BeautifulSoup
from datetime import datetime
import helpers



html = '''
		<html>
		<head>
			<title>Боевая шина: Информационная страница ИИС ЦОН</title>
			<link rel="stylesheet" type="text/css" href="/csp/sys/intersystems.css" title="Standard Style" >
			<script type="text/javascript">
			function GetCheckboxValues(cbName,elementId) {
				var idList = '';
				var checkbox = document.getElementsByName(cbName);
				for (i = 0; i < checkbox.length; i++) {
					if (checkbox[i].checked) {
						idList = idList + checkbox[i].value+';';
					}
				}
				if (idList!='') {
					document.getElementsByName(elementId)[0].value = idList
				}
			}
 
			function CheckAll(all,cbName) {
  				if (all.type == 'checkbox') {
	  				var checkbox = document.getElementsByName(cbName)
					for (i = 0; i < checkbox.length; i++) {
						checkbox[i].checked = all.checked;
					}
	  			}
			}
		   </script>
		</head>
 
		<body>
			<!-- Шапка страницы -->
			<table width="100%" height="20" cols="3">
			<tr>
				<td width="15%"/>
				<td width="70%" align="center"><h1>Боевая шина: Информационная страница ИИС ЦОН</h1></td>
				<td width="15%"/>
			</tr>
			<tr>
				<td width="15%" nowrap style="padding-left: 10px"><a href=isc.util.About.cls>[На главную]</a>&nbsp;&nbsp;&nbsp;<a href=isc.util.Map.cls>[На карту]</a></td>
				<td width="70%" nowrap align="center"><a href=?Action=26>[Авторизация в системе]</a></td>
				<td width="15%" align="right" style="padding-right: 10px"><a href="iiscon.htm">[Справка]</a></td>
			</tr>
			</table>
 
			<hr/>
 
			<!-- Вывод содержимого страницы в соответствии выбранным действием -->
<div style="padding-left: 10px;">

		<b>Основные свойства заявки</b><br>
		Услуга: Z22-74 - Выдача справки о заключении брака<br>
		Регистратор: MJ-S-Z-Z1 - Отдел №1 города Павлодар по обслуживанию населения филиала некоммерческого акционерного общества «Государственная корпорация «Правительство для граждан» по Павлодарской области<br>
		Исполнитель: MJ-S-Z-OZ - Отдел города Павлодар по РАГС филиала НАО «ГК «Правительство для граждан» по Павлодарской области

	
<table cellspacing="0" border-style="solid" border=1>
<tr>
<td>id<br></td>
<td>applicationId<br></td>
<td>serviceType<br></td>
<td>createDate<br></td>
<td>lastChangeDate<br></td>
<td>registerOrg<br></td>
<td>executorOrg<br></td>
<td>deliveryOrg<br></td>
<td>deadline<br></td>
<td>currentState<br></td>
<td>isSuspended<br></td>
<td>isPositive<br></td>
<td>isRegisterNotifyNeeded<br></td>
<td>isExecutorNotifyNeeded<br></td>
<td>versionNumber<br></td>
<td>registerId<br></td>
<td>registerDate<br></td>
<td>smsCode<br></td>
<td>cost<br></td>
<td>lang<br></td>
<td>finalDocumentLang<br></td>
<td>isPersonApplicant<br></td>
<td>paperState<br></td>
<td>suspensionStatusInfo<br></td>
<td>suspensionStatusInfoKz<br></td>
<td>registerCallDate<br></td>
<td>updateCallDate<br></td>
<td>registerXmlSignature<br></td>
<td>updateXmlSignature<br></td>
<td>registerRequestBody<br></td>
<td>updateRequestBody<br></td>
<td>applicantName<br></td>
<td>applicantGender<br></td>
<td>finishedDate<br></td>
<td>handedDate<br></td>
<td>applicantIdent<br></td>
<td>executionProcessName<br></td>
<td>executorEndpoint<br></td>
<td>sessionId<br></td>
<td>cancelDate<br></td>
<td>cancelState<br></td>
<td>cancelStatusInfo<br></td>
<td>cancelStatusInfoKz<br></td>
<td>createDateYMD<br></td>
<td>servCategory<br></td>
<td>regionCode<br></td>
<td>districtCode<br></td>
<td>deadlineDateYMD<br></td>
<td>appPrefixCode<br></td>
<td>appSourceCode<br></td>
<td>registerEmployee<br></td>
<td>regFeedback<br></td>
<td>regWaitTime<br></td>
<td>regProcTime<br></td>
<td>regPriority<br></td>
<td>isExpired<br></td>
<td>registerMethod<br></td>
<td>registerDateYMD<br></td>
<td>finishedDateYMD<br></td>
<td>handedDateYMD<br></td>
<td>applicantBirthdayYMD<br></td>
<td>applicantAge<br></td>
<td>subServiceType<br></td>
<td>applicantNameString<br></td>
<td>asEService<br></td>
<td>businessState<br></td>
<td>cancelReason<br></td>
<td>compositeId<br></td>
<td>deadlineTimeH<br></td>
<td>deadlineTimeM<br></td>
<td>deliveryId<br></td>
<td>documentDelivery<br></td>
<td>eQueueRegTicket<br></td>
<td>execFeedback<br></td>
<td>executorId<br></td>
<td>finalDocument<br></td>
<td>finishedTimeH<br></td>
<td>finishedTimeM<br></td>
<td>hasContacts<br></td>
<td>hasTrustee<br></td>
<td>isForNotification<br></td>
<td>paymentType<br></td>
<td>refuseReason<br></td>
<td>registerTimeH<br></td>
<td>registerTimeM<br></td>
<td>shepCorrelationId<br></td>
<td>subDistrictCode<br></td>
<td>usedBiometrics<br></td>
</tr>
<tr> 
<td>728229156<br></td>
<td><a href=?Action=4&appId=002269229918 target="_self">002269229918</a><br></td>
<td><a href=?Action=13&objId=10 target="_self">10</a><br></td>
<td>2025-03-17 04:16:51.345<br></td>
<td>2025-04-01 04:48:55.325<br></td>
<td><a href=?Action=9&objId=1484 target="_self">1484</a><br></td>
<td><a href=?Action=9&objId=1481 target="_self">1481</a><br></td>
<td><a href=?Action=9&objId=1484 target="_self">1484</a><br></td>
<td>2025-03-26 18:59:59.154<br></td>
<td>ACCEPTED<br></td>
<td>0<br></td>
<td><br></td>
<td>0<br></td>
<td>0<br></td>
<td>11<br></td>
<td>002269229918<br></td>
<td>2025-03-17 04:16:51.103<br></td>
<td>71<br></td>
<td>1159.2<br></td>
<td>RUS<br></td>
<td>RUS<br></td>
<td>1<br></td>
<td><br></td>
<td><br></td>
<td><br></td>
<td>2025-03-17 04:16:51.345<br></td>
<td>2025-03-17 04:24:46.039<br></td>
<td><br></td>
<td><br></td>
<td>,
      <br><b>Очередь уведомлений isc.kzcon.ens.MsgQueue</b>
<table cellspacing="0" border-style="solid" border=1>
<tr>
<td>ID<br></td>
<td>QueueName<br></td>
<td>QueueType<br></td>
<td>ApplicationId<br></td>
<td>CreateDate<br></td>
<td>CreateTime<br></td>
<td>Initiator<br></td>
<td>LastError<br></td>
<td>EnsMsg<br></td>
<td>EnsMsgClass<br></td>
<td>SoapAction<br></td>
<td>CurrentAttempt<br></td>
<td>NextAttemptTime<br></td>
<td>SendDateTime<br></td>
<td>TimeRequest<br></td>
<td>Info<br></td>
<td>CreateDT<br></td>
<td>EndPointUrl<br></td>
<td>InfoSystemName<br></td>
<td>ServiceTypeCode<br></td>
<td>cleanerDate<br></td>
</tr>
<tr>
<td>12430955321<br></td>
<td>ARMMON<br></td>
<td>1<br></td>
<td><a href=?Action=4&appId=002269229918 target="_self">002269229918</a><br></td>
<td>2025-03-17<br></td>
<td>04:16:51.503<br></td>
<td>Регистрация и обновление<br></td>
<td><br></td>
<td><a href=?Action=23&msgId=33215872563 target="_self">33215872563</a><br></td>
<td>NotificationRequest<br></td>
<td>urn:registerApplicationNotification<br></td>
<td>0<br></td>
<td><br></td>
<td>20250317 09:16:51<br></td>
<td>.234248<br></td>
<td><br></td>
<td>2025-03-17 04:16:51.503<br></td>
<td>http://mon.iiscon.kz/csp/mon/UT.Client.MON.UniversalService.cls<br></td>
<td>АРМ Мониторинг<br></td>
<td>Z22-74<br></td>
<td>2025-03-17<br></td>
</tr>
<tr>
<td>12430955343<br></td>
<td>PEP<br></td>
<td>1<br></td>
<td><a href=?Action=4&appId=002269229918 target="_self">002269229918</a><br></td>
<td>2025-03-17<br></td>
<td>04:16:51.684<br></td>
<td>Регистрация и обновление<br></td>
<td><br></td>
<td><a href=?Action=23&msgId=33215872621 target="_self">33215872621</a><br></td>
<td>NotificationRequest<br></td>
<td><br></td>
<td>0<br></td>
<td><br></td>
<td>20250317 09:16:55<br></td>
<td>1.629823<br></td>
<td><br></td>
<td>2025-03-17 04:16:51.684<br></td>
<td>http://shep2.egov.kz/bip-sync/<br></td>
<td>Личный кабинет ПЭП<br></td>
<td>Z22-74<br></td>
<td>2025-03-17<br></td>
</tr>
<tr>
<td>12430968592<br></td>
<td>ARMMON<br></td>
<td>1<br></td>
<td><a href=?Action=4&appId=002269229918 target="_self">002269229918</a><br></td>
<td>2025-03-17<br></td>
<td>04:24:49.349<br></td>
<td>Регистрация и обновление<br></td>
<td><br></td>
<td><a href=?Action=23&msgId=33215918033 target="_self">33215918033</a><br></td>
<td>NotificationRequest<br></td>
<td>urn:updateApplicationNotification<br></td>
<td>0<br></td>
<td><br></td>
<td>20250317 09:25:21<br></td>
<td>31.628208<br></td>
<td><br></td>
<td>2025-03-17 04:24:49.349<br></td>
<td>http://mon.iiscon.kz/csp/mon/UT.Client.MON.UniversalService.cls<br></td>
<td>АРМ Мониторинг<br></td>
<td>Z22-74<br></td>
<td>2025-03-17<br></td>
</tr>
<tr>
<td>12430968665<br></td>
<td>PEP<br></td>
<td>1<br></td>
<td><a href=?Action=4&appId=002269229918 target="_self">002269229918</a><br></td>
<td>2025-03-17<br></td>
<td>04:24:50.640<br></td>
<td>Регистрация и обновление<br></td>
<td><br></td>
<td><a href=?Action=23&msgId=33215918245 target="_self">33215918245</a><br></td>
<td>NotificationRequest<br></td>
<td><br></td>
<td>0<br></td>
<td><br></td>
<td>20250317 09:26:32<br></td>
<td>.850755<br></td>
<td><br></td>
<td>2025-03-17 04:24:50.640<br></td>
<td>http://shep2.egov.kz/bip-sync/<br></td>
<td>Личный кабинет ПЭП<br></td>
<td>Z22-74<br></td>
<td>2025-03-17<br></td>
</tr>
<tr>
<td>12430968825<br></td>
<td>ARMMON<br></td>
<td>1<br></td>
<td><a href=?Action=4&appId=002269229918 target="_self">002269229918</a><br></td>
<td>2025-03-17<br></td>
<td>04:24:53.290<br></td>
<td>Регистрация и обновление<br></td>
<td><br></td>
<td><a href=?Action=23&msgId=33215918717 target="_self">33215918717</a><br></td>
<td>NotificationRequest<br></td>
<td>urn:changeApplicationStatusNotification<br></td>
<td>0<br></td>
<td><br></td>
<td>20250317 09:25:22<br></td>
<td>.938056<br></td>
<td>ACCEPTED<br></td>
<td>2025-03-17 04:24:53.290<br></td>
<td>http://mon.iiscon.kz/csp/mon/UT.Client.MON.UniversalService.cls<br></td>
<td>АРМ Мониторинг<br></td>
<td>Z22-74<br></td>
<td>2025-03-17<br></td>
</tr>
<tr>
<td>12450499665<br></td>
<td>ARMMON<br></td>
<td>1<br></td>
<td><a href=?Action=4&appId=002269229918 target="_self">002269229918</a><br></td>
<td>2025-04-01<br></td>
<td>04:48:55.367<br></td>
<td>Регистрация и обновление<br></td>
<td><br></td>
<td><a href=?Action=23&msgId=33284658270 target="_self">33284658270</a><br></td>
<td>NotificationRequest<br></td>
<td>urn:changeApplicationStatusNotification<br></td>
<td>0<br></td>
<td><br></td>
<td>20250401 09:48:55<br></td>
<td>.027124<br></td>
<td><br></td>
<td>2025-04-01 04:48:55.367<br></td>
<td>http://mon.iiscon.kz/csp/mon/UT.Client.MON.UniversalService.cls<br></td>
<td>АРМ Мониторинг<br></td>
<td>Z22-74<br></td>
<td>2025-04-01<br></td>
</tr>
</table>
<br><b>Очередь гарантированного приема isc.kzcon.ens.EnsRequestQueue</b>
<table cellspacing="0" border-style="solid" border=1>
<tr>
<td>ID<br></td>
<td>QueueName<br></td>
<td>QueueType<br></td>
<td>ApplicationId<br></td>
<td>CreateDate<br></td>
<td>CreateTime<br></td>
<td>CreateDT<br></td>
<td>Initiator<br></td>
<td>LastError<br></td>
<td>EnsMsg<br></td>
<td>EnsMsgClass<br></td>
<td>CurrentAttempt<br></td>
<td>NextAttemptTime<br></td>
<td>SendDateTime<br></td>
<td>TimeRequest<br></td>
</tr>
</table>
<br><b>Очередь уведомлений isc.kzcon.ens.MsgQueue</b>
<table cellspacing="0" border-style="solid" border=1>
<tr>
<td>ID<br></td>
<td>QueueName<br></td>
<td>QueueType<br></td>
<td>ApplicationId<br></td>
<td>CreateDate<br></td>
<td>CreateTime<br></td>
<td>Initiator<br></td>
<td>LastError<br></td>
<td>EnsMsg<br></td>
<td>EnsMsgClass<br></td>
<td>SoapAction<br></td>
<td>CurrentAttempt<br></td>
<td>NextAttemptTime<br></td>
<td>SendDateTime<br></td>
<td>TimeRequest<br></td>
<td>Info<br></td>
<td>CreateDT<br></td>
<td>EndPointUrl<br></td>
<td>InfoSystemName<br></td>
<td>ServiceTypeCode<br></td>
<td>cleanerDate<br></td>
</tr>
<tr>
<td>12430955321<br></td>
<td>ARMMON<br></td>
<td>1<br></td>
<td><a href=?Action=4&appId=002269229918 target="_self">002269229918</a><br></td>
<td>2025-03-17<br></td>
<td>04:16:51.503<br></td>
<td>Регистрация и обновление<br></td>
<td><br></td>
<td><a href=?Action=23&msgId=33215872563 target="_self">33215872563</a><br></td>
<td>NotificationRequest<br></td>
<td>urn:registerApplicationNotification<br></td>
<td>0<br></td>
<td><br></td>
<td>20250317 09:16:51<br></td>
<td>.234248<br></td>
<td><br></td>
<td>2025-03-17 04:16:51.503<br></td>
<td>http://mon.iiscon.kz/csp/mon/UT.Client.MON.UniversalService.cls<br></td>
<td>АРМ Мониторинг<br></td>
<td>Z22-74<br></td>
<td>2025-03-17<br></td>
</tr>
<tr>
<td>12430955343<br></td>
<td>PEP<br></td>
<td>1<br></td>
<td><a href=?Action=4&appId=002269229918 target="_self">002269229918</a><br></td>
<td>2025-03-17<br></td>
<td>04:16:51.684<br></td>
<td>Регистрация и обновление<br></td>
<td><br></td>
<td><a href=?Action=23&msgId=33215872621 target="_self">33215872621</a><br></td>
<td>NotificationRequest<br></td>
<td><br></td>
<td>0<br></td>
<td><br></td>
<td>20250317 09:16:55<br></td>
<td>1.629823<br></td>
<td><br></td>
<td>2025-03-17 04:16:51.684<br></td>
<td>http://shep2.egov.kz/bip-sync/<br></td>
<td>Личный кабинет ПЭП<br></td>
<td>Z22-74<br></td>
<td>2025-03-17<br></td>
</tr>
<tr>
<td>12430968592<br></td>
<td>ARMMON<br></td>
<td>2<br></td>
<td><a href=?Action=4&appId=002269229918 target="_self">002269229918</a><br></td>
<td>2025-03-17<br></td>
<td>04:24:49.349<br></td>
<td>Регистрация и обновление<br></td>
<td><br></td>
<td><a href=?Action=23&msgId=33215918033 target="_self">33215918033</a><br></td>
<td>NotificationRequest<br></td>
<td>urn:updateApplicationNotification<br></td>
<td>0<br></td>
<td><br></td>
<td>20250317 09:25:21<br></td>
<td>31.628208<br></td>
<td><br></td>
<td>2025-03-17 04:24:49.349<br></td>
<td>http://mon.iiscon.kz/csp/mon/UT.Client.MON.UniversalService.cls<br></td>
<td>АРМ Мониторинг<br></td>
<td>Z22-74<br></td>
<td>2025-03-17<br></td>
</tr>
<tr>
<td>12430968665<br></td>
<td>PEP<br></td>
<td>1<br></td>
<td><a href=?Action=4&appId=002269229918 target="_self">002269229918</a><br></td>
<td>2025-03-17<br></td>
<td>04:24:50.640<br></td>
<td>Регистрация и обновление<br></td>
<td><br></td>
<td><a href=?Action=23&msgId=33215918245 target="_self">33215918245</a><br></td>
<td>NotificationRequest<br></td>
<td><br></td>
<td>0<br></td>
<td><br></td>
<td>20250317 09:26:32<br></td>
<td>.850755<br></td>
<td><br></td>
<td>2025-03-17 04:24:50.640<br></td>
<td>http://shep2.egov.kz/bip-sync/<br></td>
<td>Личный кабинет ПЭП<br></td>
<td>Z22-74<br></td>
<td>2025-03-17<br></td>
</tr>
<tr>
<td>12430968825<br></td>
<td>ARMMON<br></td>
<td>1<br></td>
<td><a href=?Action=4&appId=002269229918 target="_self">002269229918</a><br></td>
<td>2025-03-17<br></td>
<td>04:24:53.290<br></td>
<td>Регистрация и обновление<br></td>
<td><br></td>
<td><a href=?Action=23&msgId=33215918717 target="_self">33215918717</a><br></td>
<td>NotificationRequest<br></td>
<td>urn:changeApplicationStatusNotification<br></td>
<td>0<br></td>
<td><br></td>
<td>20250317 09:25:22<br></td>
<td>.938056<br></td>
<td>ACCEPTED<br></td>
<td>2025-03-17 04:24:53.290<br></td>
<td>http://mon.iiscon.kz/csp/mon/UT.Client.MON.UniversalService.cls<br></td>
<td>АРМ Мониторинг<br></td>
<td>Z22-74<br></td>
<td>2025-03-17<br></td>
</tr>
<tr>
<td>12450499665<br></td>
<td>ARMMON<br></td>
<td>1<br></td>
<td><a href=?Action=4&appId=002269229918 target="_self">002269229918</a><br></td>
<td>2025-04-01<br></td>
<td>04:48:55.367<br></td>
<td>Регистрация и обновление<br></td>
<td><br></td>
<td><a href=?Action=23&msgId=33284658270 target="_self">33284658270</a><br></td>
<td>NotificationRequest<br></td>
<td>urn:changeApplicationStatusNotification<br></td>
<td>0<br></td>
<td><br></td>
<td>20250401 09:48:55<br></td>
<td>.027124<br></td>
<td><br></td>
<td>2025-04-01 04:48:55.367<br></td>
<td>http://mon.iiscon.kz/csp/mon/UT.Client.MON.UniversalService.cls<br></td>
<td>АРМ Мониторинг<br></td>
<td>Z22-74<br></td>
<td>2025-04-01<br></td>
</tr>
</table>
<br><b>Очередь гарантированного приема isc.kzcon.ens.EnsRequestQueue</b>
<table cellspacing="0" border-style="solid" border=1>
<tr>
<td>ID<br></td>
<td>QueueName<br></td>
<td>QueueType<br></td>
<td>ApplicationId<br></td>
<td>CreateDate<br></td>
<td>CreateTime<br></td>
<td>CreateDT<br></td>
<td>Initiator<br></td>
<td>LastError<br></td>
<td>EnsMsg<br></td>
<td>EnsMsgClass<br></td>
<td>CurrentAttempt<br></td>
<td>NextAttemptTime<br></td>
<td>SendDateTime<br></td>
<td>TimeRequest<br></td>
</tr>
</table>

<br><b>История ChangeApplicationStatus</b>
<table cellspacing="0" border-style="solid" border=1>
<tr>
<td>application<br></td>
<td>cancelState<br></td>
<td>createDate<br></td>
<td>id<br></td>
<td>isPositive<br></td>
<td>isSuspended<br></td>
<td>newStatus<br></td>
<td>oldStatus<br></td>
<td>paperState<br></td>
<td>requestBody<br></td>
<td>versionNumber<br></td>
<td>xmlSignature<br></td>
</tr>
<tr>
<td>728229156<br></td>
<td><br></td>
<td>2025-03-17 04:24:51.784<br></td>
<td><a href=?Action=404&objId=2374430451 target="_self">2374430451</a><br></td>
<td><br></td>
<td><br></td>
<td>ACCEPTED<br></td>
<td>REGISTERED<br></td>
<td><br></td>
<td>.
</tr>
<tr>
<td>728229156<br></td>
<td>CANCELLED<br></td>
<td>2025-04-01 04:48:55.325<br></td>
<td><a href=?Action=404&objId=2380129103 target="_self">2380129103</a><br></td>
<td><br></td>
<td><br></td>
<td>ACCEPTED<br></td>
<td>ACCEPTED<br></td>
<td><br></td>
<td>.
</tr>



'''

soup = BeautifulSoup(html, "html.parser")
tr_list = soup.find_all('tr')
historyTable = soup.find_all("table")
# 4 то что нужно
tr = tr_list[3]
sigma = tr_list[5]
td_list = tr.find_all("td")
print(td_list[4].text, td_list[8].text, td_list[9].text)



lastModified = td_list[4].text
deadline = td_list[8].text
status = td_list[9].text

print(f"Last modified: {td_list[4].text}",
      f"Deadline: {td_list[8].text}",
      f"Status: {td_list[9].text}")

print(helpers.isMadeItInTime(lastModified, deadline))

if status == "ACCEPTED":
      print("acc")
else:
      print("not acc")

