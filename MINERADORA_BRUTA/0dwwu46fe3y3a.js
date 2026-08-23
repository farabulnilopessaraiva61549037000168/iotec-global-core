;!function(){try { var e="undefined"!=typeof globalThis?globalThis:"undefined"!=typeof global?global:"undefined"!=typeof window?window:"undefined"!=typeof self?self:{},n=(new e.Error).stack;n&&((e._debugIds|| (e._debugIds={}))[n]="c97c2e56-9c10-2d10-4ba1-dcc0fdd21fec")}catch(e){}}();
(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,476601,e=>{"use strict";var t=e.i(908796),r=e.i(761201);let n=["/home","/cycles","/usage","/account","/bounties","/templates","/learn","/repls","/replEnvironmentDesktop","/replEnvironmentMobile","/new","/profile","/templates/templates","/my-teams"];e.s(["convertDecimalToDisplayPercent",0,function(e){if(e>1)return"100%+";let t=(100*e).toLocaleString(void 0,{maximumFractionDigits:0});return`${t}%`},"getUbbSuspensionDescription",0,e=>{let n,i="";switch(e.type){case"org":if(e.orgDealContext?.dealType===t.OrgDealType.Trial||e.orgDealContext?.dealType===t.OrgDealType.EnterpriseTrial){n=e.isAdmin?`Your Replit trial has ended. Contact ${e.orgDealContext?.salesContactEmail??r.SALES_TEAM_CONTACT_EMAIL} to resume services.`:"Your Replit trial has ended. Contact your admin to resume services.";break}n=e.isSuspended?e.isAdmin?"Your workspace has been temporarily suspended due to a failed payment. Please update your workspace's payment method and address unpaid invoices to continue using Agent.":"Your workspace has been temporarily suspended due to a failed payment. Contact your admin to continue using Agent.":e.isAdmin?"Your workspace has a failed payment. Please update your workspace's payment method to continue using Agent.":"Your workspace has a failed payment. Contact your admin to continue using Agent.",i=e.isAdmin?"If you have already updated your workspace's payment method, please wait a few minutes and refresh the page.":"If your admin has already updated your workspace's payment method, please wait a few minutes and refresh the page.";break;case"user":n=e.isSuspended?"Your account has been temporarily suspended due to a failed payment":"You have a failed payment. Please update your payment method to continue using Agent.",i="If you have already updated your payment method, please wait a few minutes and refresh the page."}return{headingText:n,subheadingText:i}},"shouldShowUsageAlert",0,e=>n.includes(e)||e.startsWith("/t/[orgSlug]")])},798926,e=>{e.v({prose:"Prose-module__aikpka__prose"})},827320,e=>{"use strict";var t=e.i(276385),r=e.i(389959),n=e.i(8047),i=e.i(798926);e.s(["Prose",0,({children:e,...a})=>(0,t.jsx)(n.Text,{multiline:!0,clsx:i.default.prose,...a,children:r.Children.map(e,e=>"string"==typeof e?(0,t.jsx)("span",{children:e}):e)})])},233763,e=>{"use strict";var t=e.i(389959),r=e.i(830675),n=e.i(320216),i=e.i(871752),a=e.i(489859);let s="email-verification-resend-timestamp";e.s(["useEmailVerificationResend",0,function(){let[e,o]=(0,t.useState)(!1),[u,l]=(0,t.useState)(0),{showConfirm:c,showError:d}=(0,n.default)();return(0,t.useEffect)(()=>{try{let e=a.default.get(s,"number");if(e){let t=Date.now()-e;t<6e4?(o(!0),l(Math.ceil((6e4-t)/1e3))):a.default.remove(s)}}catch(e){r.captureException(e)}},[]),(0,t.useEffect)(()=>{if(!e||u<=0)return;let t=setInterval(()=>{l(e=>{let n=e-1;if(n<=0){o(!1);try{a.default.remove(s)}catch(e){r.captureException(e)}return clearInterval(t),0}return n})},1e3);return()=>clearInterval(t)},[e,u]),{resendVerification:(0,t.useCallback)(async()=>{if(!e)try{await (0,i.postJson)("/data/user/resend_verification",{}),c("Verification email sent"),o(!0),l(60);try{a.default.set(s,Date.now())}catch(e){r.captureException(e)}}catch(t){let{message:e}=t;d(`Failed to resend verification email: ${e}`),r.captureException(t)}},[e,c,d]),isInCooldown:e,cooldownTimeRemaining:u}}])},535211,e=>{"use strict";var t=e.i(389959),r=e.i(973245),n=e.i(304277);e.i(566901);let i={},a=r.gql`
    query PollEmailVerification {
  currentUser {
    id
    isVerified
  }
}
    `;e.s(["default",0,e=>{let r,s=(0,t.useRef)(e?.onEmailVerified),o=(0,t.useRef)(e?.onError),u=(0,t.useCallback)(()=>{s.current&&s.current()},[]),l=(0,t.useCallback)(e=>{o.current&&o.current(e)},[]),{loading:c,data:d,error:p,startPolling:m,stopPolling:g}=(r={...i,...void 0},n.useQuery(a,r));return(0,t.useEffect)(()=>(m(2e3),()=>g()),[m,g]),(0,t.useEffect)(()=>{if(p){g(),l&&l(p);return}d&&d.currentUser?.isVerified&&(g(),u&&u())},[d,p,g,l,u]),{loading:c,error:p,isVerified:d?.currentUser?.isVerified}}],535211)},350095,e=>{"use strict";var t=e.i(973245),r=e.i(304277);e.i(566901);let n={},i=t.gql`
    query EmailVerificationContent {
  currentUser {
    id
    email
  }
}
    `;e.s(["useEmailVerificationContentQuery",0,function(e){let t={...n,...e};return r.useQuery(i,t)}])},586964,e=>{e.v({cooldownText:"EmailVerificationContent-module__QdUitG__cooldownText",textCenter:"EmailVerificationContent-module__QdUitG__textCenter"})},899554,e=>{"use strict";var t=e.i(276385);e.i(155865);var r=e.i(350095),n=e.i(269848),i=e.i(11029),a=e.i(233763);e.i(871752);var s=e.i(919073),o=e.i(643484),u=e.i(8047),l=e.i(244945),c=e.i(61732),d=e.i(586964);let p=({title:e="Please verify your email address",subtitle:p}={})=>{let{loading:m,data:g}=(0,r.useEmailVerificationContentQuery)(),{resendVerification:f,isInCooldown:y,cooldownTimeRemaining:h}=(0,a.useEmailVerificationResend)();return(0,t.jsxs)(c.View,{gap:24,align:"center","data-cy":"email-verification-widget",children:[(0,t.jsxs)(c.View,{gap:8,align:"center",children:[(0,t.jsx)(u.Header,{level:2,variant:"headerDefault",clsx:d.default.textCenter,children:e}),p?(0,t.jsx)(u.Text,{clsx:d.default.textCenter,variant:"small",children:p}):null]}),(0,t.jsxs)(u.Text,{clsx:d.default.textCenter,children:["We sent an email to"," ",m?(0,t.jsx)(n.default,{}):(0,t.jsx)(u.Text,{style:{textDecoration:"underline",textUnderlineOffset:"3px"},children:g?.currentUser?.email}),"."]}),(0,t.jsxs)(c.View,{row:!0,gap:8,children:[(0,t.jsxs)(s.ShadesSurface,{children:[(0,t.jsx)(l.Tooltip,{tooltip:`You can resend in ${h} seconds`,placement:"bottom",isDisabled:!y,children:(0,t.jsx)(o.Button,{iconLeft:(0,t.jsx)(i.default,{}),onClick:f,text:"Resend email",variant:"outlined",disabled:y})}),y?(0,t.jsxs)(u.Text,{variant:"small",color:"dimmer",clsx:d.default.cooldownText,children:["You can resend in ",h," seconds"]}):null]}),!1]}),(0,t.jsx)(u.Text,{clsx:d.default.textCenter,variant:"small",textWrap:"balance",children:"Don't see an email? Check your spam or other filtered folders."})]})};var m=e.i(535211),g=e.i(320216);e.s(["default",0,({onEmailVerified:e,...r})=>{let{showConfirm:n,showError:i}=(0,g.default)();return(0,m.default)({onEmailVerified:()=>{n("Email verified!"),e?.()},onError:e=>{i(e.message)}}),(0,t.jsx)(p,{...r})}],899554)},443505,e=>{"use strict";var t=e.i(389959),r=e.i(753451),n=e.i(584878);e.s(["default",0,function({onChange:e}){let i=(0,r.useIsInBonsaiWebview)();(0,t.useEffect)(()=>{if(!i)return;let t=t=>(0,n.payingStatusChangedBridgeMessageHandler)(t,()=>{e()});return window.addEventListener("message",t),()=>{window.removeEventListener("message",t)}},[i,e])}])},638141,e=>{"use strict";var t=e.i(488081),r=e.i(389959),n=e.i(179104),i=e.i(134628),a=e.i(753451),s=e.i(584878);e.s(["default",0,function(){let e=(0,t.useRouter)(),o=(0,a.doesBonsaiWebviewSupportFeature)(e,"stripePayment")&&(0,a.isInBonsaiWebview)(e);return{showPaymentFlow:(0,r.useCallback)(e=>{let t={messageType:i.BridgeMessageType.SHOW_PAYMENT_FLOW,flow:e};switch(e.type){case"setup":if(!o)break;(0,s.sendMessage)(t,(0,n.nanoid)());break;case"setUsageLimits":(0,s.sendMessage)(t,(0,n.nanoid)())}},[o])}}])},518726,e=>{"use strict";var t=e.i(973245),r=e.i(951262),n=e.i(304277),i=e.i(566901);let a={},s=t.gql`
    fragment CurrentUserPaymentMethod on CurrentUser {
  paymentMethod {
    ... on PaymentMethod {
      id
      externalId
      last4
      expirationMonth
      expirationYear
    }
    ... on UnauthorizedError {
      message
    }
  }
}
    `,o=t.gql`
    mutation CreateStripeSetupIntent($input: CreateSetupIntentInput!) {
  createSetupIntent(input: $input) {
    ... on CreateSetupIntentResult {
      clientSecret
    }
    ... on UnauthorizedError {
      message
    }
    ... on UserError {
      message
    }
    ... on TooManyRequestsError {
      message
    }
  }
}
    `,u=t.gql`
    query SetupIntentFormCurrentUserEmailVerification {
  currentUser {
    id
    isVerified
  }
}
    `,l=t.gql`
    query PollPaymentMethod {
  currentUser {
    id
    ...CurrentUserPaymentMethod
  }
}
    ${s}`;e.s(["useCreateStripeSetupIntentMutation",0,function(e){let t={...a,...e};return r.useMutation(o,t)},"usePollPaymentMethodLazyQuery",0,function(e){let t={...a,...e};return i.useLazyQuery(l,t)},"useSetupIntentFormCurrentUserEmailVerificationQuery",0,function(e){let t={...a,...e};return n.useQuery(u,t)}])},417137,e=>{"use strict";var t=e.i(973245),r=e.i(304277);e.i(566901);let n={},i=t.gql`
    query IsOnTrialPlan {
  currentUser {
    id
    userSubscriptionType
    userSubscription {
      isTrial
    }
    billingInfo {
      planInfo {
        cancelAt
      }
    }
  }
}
    `;var a=e.i(908796);e.s(["useIsOnTrialPlan",0,e=>{let t,{data:s,...o}=(t={...n,...e},r.useQuery(i,t)),u=s?.currentUser?.userSubscriptionType===a.UserSubscriptionTypeEnum.HackerPro,l=s?.currentUser?.userSubscription?.isTrial??!1,c=l&&!!s?.currentUser?.billingInfo?.planInfo?.cancelAt;return{...o,isOnTrialPlan:l,trialWillCancel:c,isPro:u}}],417137)},721368,e=>{"use strict";var t=e.i(912024);let r={return_url:window.location.href};e.s(["basicStripeElementsOptions",0,{currency:"usd",payment_method_types:["card"]},"generateStripeErrorMessage",0,function(e){return("card_error"===e.type||"validation_error"===e.type||"invalid_request_error"===e.type)&&e.message?e.message:((0,t.captureSentryException)(`Stripe Elements error: ${e.message??"unknown"}`,{extra:{message:e.message,type:e.type,code:e.code,declineCode:e.decline_code,docUrl:e.doc_url,paymentIntent:e.payment_intent,paymentMethod:e.payment_method,setupIntent:e.setup_intent,source:e.source}}),"Something went wrong. Please contact support.")},"getStripeElementsConfirmParams",0,function(e){return e?{return_url:e}:r},"stripeElementsConfirmParams",0,r])},738711,e=>{e.v({fullHeight:"NewPaymentMethodForm-module__mblimG__fullHeight"})},590563,e=>{"use strict";var t=e.i(276385),r=e.i(518726),n=e.i(416746),i=e.i(596139),a=e.i(912024),s=e.i(621936),o=e.i(417137),u=e.i(721368),l=e.i(899554),c=e.i(753451),d=e.i(415541),p=e.i(709485),m=e.i(443505),g=e.i(638141),f=e.i(108431),y=e.i(61732),h=e.i(738711);e.s(["NewPaymentMethodForm",0,function({onClose:e,context:x,powerUpCategory:v,children:S,buttonText:b,buttonIcon:C,returnUrl:w}){let T=(0,c.useDoesBonsaiWebviewSupportFeature)("stripePayment"),{data:j}=(0,r.useSetupIntentFormCurrentUserEmailVerificationQuery)({skip:T}),{showPaymentFlow:_}=(0,g.default)(),{isOnTrialPlan:E,isPro:U,trialWillCancel:O}=(0,o.useIsOnTrialPlan)(),[P]=(0,r.useCreateStripeSetupIntentMutation)(),[M,{stopPolling:k}]=(0,r.usePollPaymentMethodLazyQuery)();if((0,m.default)({onChange:M}),T)return _({type:"setup",source:x??"new_payment_method_form"}),e(),null;async function I({stripe:t,elements:r,onError:n,onSubmitComplete:i}){let{error:s}=await r.submit();s?n((0,u.generateStripeErrorMessage)(s)):P({variables:{input:{}},onError:e=>{n(e.message),(0,a.captureSentryException)("Error in NewPaymentMethodForm when creating Setup Intent: "+e.message)},onCompleted:async({createSetupIntent:a})=>{if("CreateSetupIntentResult"!==a.__typename)return void n(a.message);let{error:s,setupIntent:o}=await t.confirmSetup({elements:r,clientSecret:a.clientSecret,confirmParams:(0,u.getStripeElementsConfirmParams)(w),redirect:"if_required"});s?n((0,u.generateStripeErrorMessage)(s)):null===o.payment_method||"string"!=typeof o.payment_method?n("Something went wrong. Please try again."):function({onError:t,onSubmitComplete:r,newPaymentMethod:n}){k(),M({fetchPolicy:"cache-and-network",ssr:!1,pollInterval:1500,onCompleted:i=>{i?.currentUser?.paymentMethod?.__typename==="UnauthorizedError"&&(k(),t(i.currentUser.paymentMethod.message)),i?.currentUser?.paymentMethod?.__typename==="PaymentMethod"&&i?.currentUser?.paymentMethod?.externalId===n&&(k(),(0,d.track)(p.events.PAYMENT_METHOD_FORM_USED,{action:"payment_method_saved",context:x,powerUpCategory:v}),r(),setTimeout(()=>{e()},1e3))},onError:e=>{k(),t(e.message)}})}({onSubmitComplete:i,onError:n,newPaymentMethod:o.payment_method})}})}return j?.currentUser?.isVerified===!1?(0,t.jsx)(y.View,{clsx:h.default.fullHeight,align:"center",justify:"center",children:(0,t.jsx)(l.default,{})}):(0,t.jsxs)(y.View,{gap:8,children:[E&&!O?(0,t.jsx)(f.StatusBanner,{colorway:"primary",icon:(0,t.jsx)(n.default,{}),text:(0,t.jsxs)(t.Fragment,{children:["Adding a payment method will set your Replit"," ",U?i.corePlanName:i.hackerPlanName," membership to auto-renew at the end of the trial. Cancel anytime from your"," ",(0,t.jsx)("a",{href:"/account#billing",target:"_blank",children:"account settings"}),"."]})}):null,(0,t.jsx)(s.default,{elementsOptions:{...u.basicStripeElementsOptions,mode:"setup"},isPayment:!1,onSubmit:I,submitButtonText:b??"Save payment method",submitButtonIcon:C,disclaimerTextAction:"adding this payment method",context:x,powerUpCategory:v,children:S})]})}])},366471,e=>{e.v({buttonContainer:"UBBSuspensionGracePeriod-module__oeX6Ia__buttonContainer",usageList:"UBBSuspensionGracePeriod-module__oeX6Ia__usageList"})},565282,e=>{"use strict";var t=e.i(276385),r=e.i(389959),n=e.i(138716),i=e.i(549645),a=e.i(706323),s=e.i(416298),o=e.i(590563),u=e.i(480028),l=e.i(643484),c=e.i(419635),d=e.i(488299),p=e.i(827320),m=e.i(8047),g=e.i(61732),f=e.i(366471);function y({onDone:e,onBack:r}){return(0,t.jsxs)(g.View,{gap:16,children:[(0,t.jsxs)(g.View,{row:!0,gap:8,align:"center",children:[(0,t.jsx)(d.IconButton,{alt:"Back",onClick:r,children:(0,t.jsx)(n.default,{})}),(0,t.jsx)(m.Text,{variant:"subheadDefault",multiline:!1,children:"Update Payment Method"})]}),(0,t.jsx)(o.NewPaymentMethodForm,{onClose:e,context:"suspension_grace_period"})]})}e.s(["PaymentMethodForm",0,y,"UBBSuspensionGracePeriod",0,function({suspensionScheduledTime:e,onDone:n,customerName:o,customerId:d}){let[h,x]=(0,r.useState)(!1);if(h)return(0,t.jsx)(y,{onDone:n,onBack:()=>x(!1)});let v=e?new Date(e).toLocaleString("en-US",{month:"2-digit",day:"2-digit",year:"numeric",hour:"numeric",minute:"2-digit",hour12:!0}):null,S=`/orb-customer-portal/customer/${d}`;return(0,t.jsxs)(g.View,{p:16,gap:16,children:[(0,t.jsxs)(g.View,{row:!0,gap:8,align:"center",children:[(0,t.jsx)(s.default,{size:20,color:u.tokens.orangeStronger}),(0,t.jsx)(m.Text,{variant:"subheadDefault",children:"Payment required to avoid suspension"})]}),(0,t.jsxs)(g.View,{gap:16,children:[(0,t.jsxs)(m.Text,{children:["Your recent payment for ",o," didn't go through. To prevent an interruption in services, please update the payment method or pay the outstanding balance directly."]}),(0,t.jsxs)(p.Prose,{children:[(0,t.jsx)(m.Text,{children:"What this means:"}),(0,t.jsxs)("ul",{clsx:f.default.usageList,children:[(0,t.jsx)("li",{children:"New deployments and AI services are unavailable until payment is cleared."}),(0,t.jsxs)("li",{children:["If payment is not made",v?` by ${v}`:"",", active deployments will be suspended and taken offline."]})]})]}),(0,t.jsxs)(g.View,{clsx:f.default.buttonContainer,row:!0,gap:16,justify:"space-between",children:[(0,t.jsx)(g.View,{gap:8,children:(0,t.jsx)(c.ButtonLink,{iconLeft:(0,t.jsx)(a.default,{}),text:"View and pay invoices",href:S,target:"_blank"})}),(0,t.jsx)(g.View,{gap:8,children:(0,t.jsx)(l.Button,{iconLeft:(0,t.jsx)(i.default,{}),text:"Update payment method",colorway:"primary",onClick:()=>x(!0)})})]})]})]})}])},935984,e=>{"use strict";var t=e.i(973245),r=e.i(304277),n=e.i(566901),i=e.i(951262);let a={},s=t.gql`
    fragment TourServiceTour on TourSeen {
  id
  seen
}
    `,o=t.gql`
    query TourServiceToursSeen($tours: [String!]!) {
  currentUser {
    id
    toursSeen(tours: $tours) {
      id
      ...TourServiceTour
    }
  }
}
    ${s}`,u=t.gql`
    mutation TourServiceDismissTour($name: String!) {
  markTourAsSeen2(input: {name: $name}) {
    __typename
    ... on TourSeen {
      id
      ...TourServiceTour
    }
    ... on UserError {
      message
    }
    ... on UnauthorizedError {
      message
    }
  }
}
    ${s}`;e.s(["TourServiceDismissTourDocument",0,u,"TourServiceToursSeenDocument",0,o,"useTourServiceDismissTourMutation",0,function(e){let t={...a,...e};return i.useMutation(u,t)},"useTourServiceToursSeenLazyQuery",0,function(e){let t={...a,...e};return n.useLazyQuery(o,t)},"useTourServiceToursSeenQuery",0,function(e){let t={...a,...e};return r.useQuery(o,t)}])},777198,e=>{"use strict";var t=e.i(389959),r=e.i(935984);function n(e,n){let{data:i,loading:a}=(0,r.useTourServiceToursSeenQuery)({variables:{tours:e}}),[s,{loading:o}]=(0,r.useTourServiceDismissTourMutation)({variables:{name:e},optimisticResponse:{__typename:"RootMutationType",markTourAsSeen2:{__typename:"TourSeen",id:e,seen:!0}},onCompleted:n}),[u,{loading:l}]=(0,r.useTourServiceDismissTourMutation)({variables:{name:e},optimisticResponse:{__typename:"RootMutationType",markTourAsSeen2:{__typename:"TourSeen",id:e,seen:!1}}}),c=!!i?.currentUser?.toursSeen[0].seen;return(0,t.useMemo)(()=>({isLoading:a,isDone:c,setAsDone:s,unsetAsDone:u,isMutating:o||l}),[a,c,s,u,o,l])}e.s(["useDismissibleElement",0,function(e){let{isLoading:t,isDone:r,setAsDone:i,unsetAsDone:a}=n(e);return{isLoading:t,isDone:r,setAsDone:i,unsetAsDone:a}},"useMemoedDismissibleElement",0,n])},871752,e=>{"use strict";var t=e.i(324753),r=e.i(272391);function n(e,r){return(0,t.default)(e,{credentials:"same-origin",headers:{"Content-Type":"application/json",Accept:"application/json","X-Requested-With":"XMLHttpRequest"},method:"post",body:JSON.stringify(r)})}e.s(["postJson",0,function(e,t={}){var i,a;let s;return i=n(e,t),a=e,s=new r.default("Unknown http error"),Promise.resolve(i).then(async e=>{let t;if(e.ok)return e.json();let r=e.headers.get("content-type");if(r&&r.includes("application/json"))t=await e.json();else{let r=await e.text();try{t=JSON.parse(r)}catch(e){t={message:r}}}throw t.message&&(s.message=t.message),s.setExtras({url:a,responseBody:t,responseData:{status:e.status,statusText:e.statusText,redirected:e.redirected,type:e.type,url:e.url}}).setTag("httpError","true"),s})},"wrapPost",0,n])},151027,873054,672220,284693,e=>{"use strict";var t=e.i(276385),r=e.i(488081),n=e.i(389959),i=e.i(973245);let a=i.gql`
    fragment OrgFlagsOrg on Org {
  id
  flags {
    id
    type
    value
  }
}
    `;e.s(["OrgFlagsOrgFragmentDoc",0,a],873054);var s=e.i(304277);e.i(566901);var o=e.i(951262);let u={},l=i.gql`
    fragment CurrentUserOrg on Org {
  id
  slug
  currentUserRole
  dealContext {
    dealType
    salesContactEmail
  }
  ...OrgFlagsOrg
}
    ${a}`,c=i.gql`
    query CurrentUserOrgContext {
  getUserOrgContext2 {
    ... on Org {
      ...CurrentUserOrg
    }
  }
}
    ${l}`;function d(e){let t={...u,...e};return s.useQuery(c,t)}let p=i.gql`
    query CurrentUserOrgContextGetOrg($orgSlug: String!) {
  currentUser {
    id
    org(orgSlug: $orgSlug) {
      ... on Org {
        id
        ...CurrentUserOrg
      }
      ... on Error {
        message
      }
    }
  }
}
    ${l}`;function m(e){let t={...u,...e};return s.useQuery(p,t)}let g=i.gql`
    mutation CurrentUserOrgContextUpdateOrgContext($input: UpdateOrgContextInput!) {
  updateOrgContext(input: $input) {
    ... on Org {
      ...CurrentUserOrg
    }
    ... on Error {
      __typename
      message
    }
  }
}
    ${l}`;e.s(["CurrentUserOrgContextDocument",0,c,"CurrentUserOrgContextUpdateOrgContextDocument",0,g,"useCurrentUserOrgContextGetOrgQuery",0,m,"useCurrentUserOrgContextQuery",0,d,"useCurrentUserOrgContextUpdateOrgContextMutation",0,function(e){let t={...u,...e};return o.useMutation(g,t)}],672220),e.i(908796);let f={"flag-sponsorship-bulk-send":"number","flag-org-depl-rules":"boolean","flag-require-git-remote":"boolean","flag-agent-billing-v2-teams":"boolean","flag-org-stack-templates":"boolean","flag-tom-riddle":"boolean","flag-deployments-switch-to-azure":"boolean","flag-experimental-connectors":"string","flag-org-require-security-scan-in-deployment":"boolean","flag-enable-deployment-private-passwords":"boolean","flag-org-custom-mcp-servers":"boolean","flag-org-predefined-mcp-providers":"boolean","flag-org-budgets":"boolean","flag-azure-org-can-use-object-store":"boolean","flag-unified-plans-enterprise":"boolean","flag-self-hosted-git-domains":"boolean","flag-databricks-apps":"boolean","flag-enterprise-deployment-geography-whitelist":"boolean","flag-deployment-geography-selection":"boolean"};function y(e){if(!e||"object"!=typeof e)return!1;let{id:t,type:r,value:n}=e;if(!(t in f))return!1;let i=f[t];return r===i||"number"===i&&"string"===r&&!isNaN(Number(n))}function h(e){return(e.flags||[]).filter(y).reduce((e,{id:t,value:r})=>({...e,[t]:"number"===f[t]?Number(r):r}),{})}e.s(["orgFlags",0,h],284693);var x=e.i(933302);let v=["/evaluations","/import","/integrations","/notifications","/templates","/theme","/@","/~/cli","/grab"],S=(0,n.createContext)(null),b=(0,n.createContext)(null);function C(){let e=(0,n.useContext)(S);if(null===e)throw Error("StoredOrgContextProvider missing!");return e}e.s(["StoredOrgContextProvider",0,function({children:e}){let i=(0,r.useRouter)(),a=i.asPath,s=function(){let e=(0,r.useRouter)().asPath.split("?")[0];if(e.startsWith("/t")){let t=e.split("/");if(t[2])return t[2]}return null}(),o=(0,x.useSyncStatsigOrgContext)(),u=null!=s,l=!u&&v.some(e=>a.startsWith(e)),c=d({skip:"/replEnvironmentDesktop"===i.pathname||"/replEnvironmentMobile"===i.pathname||!l}),p=c.data?.getUserOrgContext2?.__typename==="Org"?c.data.getUserOrgContext2:null,g=m({skip:!u,variables:{orgSlug:s??""}}),f=g.data?.currentUser?.org?.__typename==="Org"?g.data.currentUser.org:null,y=l?c.loading:g.loading,C=u?f:l?p:null;o(C?.id,C?.dealContext?.dealType);let[w,T]=(0,n.useState)({orgId:C?.id,orgSlug:C?.slug,orgRole:C?.currentUserRole??void 0,orgDealContext:C?.dealContext??void 0});(0,n.useEffect)(()=>{y||T({orgId:C?.id,orgSlug:C?.slug,orgRole:C?.currentUserRole??void 0,orgDealContext:C?.dealContext??void 0})},[C,y]);let j=(0,n.useCallback)(e=>T(e),[]),_=(0,n.useMemo)(()=>C?h(C):{},[C]);return(0,t.jsx)(b.Provider,{value:j,children:(0,t.jsx)(S.Provider,{value:{flags:_,orgId:w.orgId,orgSlug:w.orgSlug,orgRole:w.orgRole,orgDealContext:w.orgDealContext,loading:y},children:e})})},"getOrgTrackingContext",0,e=>e?`Org:${e.id}`:"Personal","useCurrentUserStoredOrgContext",0,C,"useIsCurrentOrgEnterprise",0,function(){let e=C();return e.orgDealContext?.dealType==="enterprise"||e.orgDealContext?.dealType==="enterprise_trial"},"useSetOptimisticOrg",0,function(){let e=(0,n.useContext)(b);if(null===e)throw Error("StoredOrgContextProvider missing!");return e}],151027)},416746,e=>{"use strict";var t=e.i(276385),r=e.i(983420);e.s(["default",0,function(e){return(0,t.jsxs)(r.default,{...e,children:[(0,t.jsx)("path",{d:"M12 11.25a.75.75 0 0 1 .75.75v4a.75.75 0 0 1-1.5 0v-4a.75.75 0 0 1 .75-.75ZM12.01 7.25a.75.75 0 0 1 0 1.5H12a.75.75 0 0 1 0-1.5h.01Z"}),(0,t.jsx)("path",{fillRule:"evenodd",d:"M12 1.25c5.937 0 10.75 4.813 10.75 10.75S17.937 22.75 12 22.75 1.25 17.937 1.25 12 6.063 1.25 12 1.25Zm0 1.5a9.25 9.25 0 1 0 0 18.5 9.25 9.25 0 0 0 0-18.5Z",clipRule:"evenodd"})]})}])},442966,e=>{"use strict";var t=e.i(276385),r=e.i(983420);e.s(["default",0,function(e){return(0,t.jsx)(r.default,{...e,children:(0,t.jsx)("path",{fillRule:"evenodd",d:"M13.376 1.253c.21-.02.422.012.616.096l.095.046.091.053c.178.115.323.274.423.46l.045.096.038.099a1.25 1.25 0 0 1 .01.755l-1.92 6.02c-.003.011-.007.023-.012.034a.253.253 0 0 0 .03.23.25.25 0 0 0 .206.108H20l.123.004a1.752 1.752 0 0 1 1.24 2.849.73.73 0 0 1-.045.05l-9.9 10.199v-.001a1.25 1.25 0 0 1-2.122-1.18l.01-.03 1.92-6.019.012-.035a.251.251 0 0 0-.12-.309.255.255 0 0 0-.056-.02l-.06-.008H4a1.752 1.752 0 0 1-1.363-2.852l.045-.05 9.9-10.2a1.25 1.25 0 0 1 .689-.38l.104-.015Zm-9.582 11.6a.252.252 0 0 0-.023.255.25.25 0 0 0 .227.142h7.001l.21.013a1.75 1.75 0 0 1 1.53 1.518c.034.269.003.54-.086.795l.002.001-1.591 4.986 9.14-9.418a.249.249 0 0 0 .047-.116.252.252 0 0 0-.115-.24.249.249 0 0 0-.064-.03l-.07-.009H13a1.753 1.753 0 0 1-1.74-1.531 1.752 1.752 0 0 1 .086-.797l1.588-4.985-9.14 9.417Z",clipRule:"evenodd"})})}])},138716,e=>{"use strict";var t=e.i(276385),r=e.i(983420);e.s(["default",0,function(e){return(0,t.jsx)(r.default,{...e,children:(0,t.jsx)("path",{fillRule:"evenodd",d:"M4.47 11.47a.75.75 0 0 0 0 1.06l7 7a.75.75 0 1 0 1.06-1.06l-5.72-5.72H19a.75.75 0 0 0 0-1.5H6.81l5.72-5.72a.75.75 0 0 0-1.06-1.06l-7 7Z",clipRule:"evenodd"})})}])},931297,(e,t,r)=>{t.exports=function(e){var t=typeof e;return null!=e&&("object"==t||"function"==t)}},481311,(e,t,r)=>{t.exports=e.g&&e.g.Object===Object&&e.g},19948,(e,t,r)=>{var n=e.r(481311),i="object"==typeof self&&self&&self.Object===Object&&self;t.exports=n||i||Function("return this")()},95645,(e,t,r)=>{t.exports=e.r(19948).Symbol},682605,(e,t,r)=>{var n=e.r(95645),i=Object.prototype,a=i.hasOwnProperty,s=i.toString,o=n?n.toStringTag:void 0;t.exports=function(e){var t=a.call(e,o),r=e[o];try{e[o]=void 0;var n=!0}catch(e){}var i=s.call(e);return n&&(t?e[o]=r:delete e[o]),i}},209928,(e,t,r)=>{var n=Object.prototype.toString;t.exports=function(e){return n.call(e)}},702114,(e,t,r)=>{var n=e.r(95645),i=e.r(682605),a=e.r(209928),s=n?n.toStringTag:void 0;t.exports=function(e){return null==e?void 0===e?"[object Undefined]":"[object Null]":s&&s in Object(e)?i(e):a(e)}},588631,(e,t,r)=>{t.exports=function(e){return null!=e&&"object"==typeof e}},280041,(e,t,r)=>{var n=e.r(702114),i=e.r(588631);t.exports=function(e){return"symbol"==typeof e||i(e)&&"[object Symbol]"==n(e)}},253044,e=>{e.v({message:"ServerError-module__3NQRmq__message",wrapper:"ServerError-module__3NQRmq__wrapper"})},412947,390189,e=>{"use strict";var t=e.i(276385),r=e.i(389959),n=e.i(830675),i=e.i(488081),a=e.i(416298),s=e.i(632350),o=e.i(753451),u=e.i(643484),l=e.i(8047),c=e.i(61732),d=e.i(253044);function p(){let e=(0,i.useRouter)(),r=(0,s.default)();return(0,t.jsx)(c.View,{clsx:d.default.wrapper,align:"center",justify:"center",children:(0,t.jsxs)(c.View,{align:"center",justify:"center",gap:16,children:[(0,t.jsx)(a.default,{size:32}),(0,t.jsx)(l.Text,{variant:"subheadDefault",clsx:d.default.message,children:(0,o.isInBonsaiWebview)(e)?" We encountered an error. Please tell us what happened by shaking your phone and submitting a bug report.":"We encountered an error. Please tell us what happened by submitting a ticket via the get help button above."}),r?(0,t.jsx)(u.Button,{text:"Return to home",colorway:"primary",onClick:()=>{window.location.href="/desktopApp/home"}}):null]})})}e.s(["default",0,p],390189);class m extends r.Component{constructor(e){super(e),this.state={hasError:!1,error:null}}static getDerivedStateFromError(e){return{hasError:!0,error:e}}componentDidCatch(e,t){n.withScope(r=>{r.setTag(this.props.sentryTag,!0),r.setExtra("errorInfo",t),r.setContext("react",{componentStack:t.componentStack}),n.captureException(e)})}render(){return this.state.hasError?this.props.fallback&&this.state.error?this.props.fallback(this.state.error):(0,t.jsx)(p,{}):this.props.children}}e.s(["default",()=>m],412947)}]);

//# debugId=c97c2e56-9c10-2d10-4ba1-dcc0fdd21fec
//# sourceMappingURL=078_c5r.50qdb.js.map
