;!function(){try { var e="undefined"!=typeof globalThis?globalThis:"undefined"!=typeof global?global:"undefined"!=typeof window?window:"undefined"!=typeof self?self:{},n=(new e.Error).stack;n&&((e._debugIds|| (e._debugIds={}))[n]="a2a6e69b-ab4e-f148-9e65-45b7607ec356")}catch(e){}}();
(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,595996,e=>{"use strict";var t=e.i(276385),n=e.i(389959),o=e.i(983420),r=e.i(967629),s=e.i(919073),a=e.i(691636),i=e.i(61732),c=e.i(727223);let l=(0,r.css)([a.rcss.overflow("hidden"),a.rcss.position.relative]),u={16:4,20:4,24:4,32:4,36:4,48:4,64:8,84:16};function d(e){let r=(0,n.useContext)(o.IconContext),{size:d=r.size??32,alt:p=r.alt??"",iconUrl:g}=e,C=d<32?4:8;function f(){return(0,t.jsx)(i.View,{css:{position:"absolute",top:0,left:0,width:"100%",height:"100%",boxShadow:"inset 0px 0px 0px 1px #80808040",borderRadius:C}})}if(g.endsWith(".svg")){let e=u[d],n=d-2*e;return(0,t.jsxs)(s.ShadesSurface,{css:[a.rcss.p(e),a.rcss.borderRadius(C),l,a.rcss.width(d),a.rcss.height(d)],children:[(0,t.jsx)(i.View,{css:[a.rcss.position.relative,a.rcss.width(n),a.rcss.height(n)],children:(0,t.jsx)(c.default,{alt:p,src:g,objectFit:"contain",layout:"fill"})}),(0,t.jsx)(f,{})]})}return(0,t.jsxs)(s.ShadesSurface,{css:[l,a.rcss.borderRadius(C),a.rcss.width(d),a.rcss.height(d)],children:[(0,t.jsx)(c.default,{alt:p,src:g,width:d,height:d,objectFit:"cover"}),(0,t.jsx)(f,{})]})}e.s(["ReplIconWithPlaceholder",0,function({isLoading:e,alt:n,iconUrl:o,size:r=32}){let i=o&&void 0!==n?(0,t.jsx)(d,{alt:n,iconUrl:o,size:r}):null;if(!e&&i)return i;let c=r<32?4:8;return(0,t.jsx)(s.ShadesSurface,{css:[l,a.rcss.borderRadius(c),a.rcss.width(r),a.rcss.height(r)]})},"default",0,d])},335451,366541,e=>{"use strict";var t=e.i(973245),n=e.i(304277);e.i(566901);let o={},r=t.gql`
    fragment ConnectorContextReplInfo on Repl {
  id
  title
  iconUrl
  url
  timeCreated
  user {
    id
    username
    fullName
    image
  }
}
    `,s=t.gql`
    fragment ConnectorContextConnectionInfo on OintConnection {
  connectionId
  connectorName
  displayName
  iconPath
  status
  type
  environment
  webhookProvider
  repls {
    ...ConnectorContextReplInfo
  }
  predefinedProvider {
    id
    displayName
    description
    baseUrl
    iconPath
  }
}
    ${r}`,a=t.gql`
    fragment ConnectorContext on CurrentUserConnectorContext {
  openIntClientToken
  connectorWhitelist
  connections {
    ...ConnectorContextConnectionInfo
  }
  connectorConfigs {
    id
    type
    connectorName
    displayName
    description
    iconPath
    webhookEvents {
      name
      model
      description
    }
  }
}
    ${s}`,i=t.gql`
    fragment OrgConnectorContext on OrgConnectorContext {
  openIntClientToken
  connectorWhitelist
  connections {
    ...ConnectorContextConnectionInfo
  }
  connectorConfigs {
    id
    type
    connectorName
    displayName
    description
    iconPath
    webhookEvents {
      name
      model
      description
    }
  }
}
    ${s}`,c=t.gql`
    query GetConnectorContext {
  currentUser {
    ... on CurrentUser {
      id
      isSubscribed
      connectorContext {
        ...ConnectorContext
      }
    }
  }
}
    ${a}`,l=t.gql`
    query GetConnectorContextByOrg($orgId: String!) {
  currentUser {
    ... on CurrentUser {
      id
      isSubscribed
      org(orgId: $orgId) {
        __typename
        ... on Org {
          id
          connectorContext {
            ...OrgConnectorContext
          }
        }
        ... on Error {
          __typename
          message
        }
      }
    }
  }
}
    ${i}`;e.s(["ConnectorContextConnectionInfoFragmentDoc",0,s,"ConnectorContextFragmentDoc",0,a,"ConnectorContextReplInfoFragmentDoc",0,r,"GetConnectorContextByOrgDocument",0,l,"GetConnectorContextDocument",0,c,"OrgConnectorContextFragmentDoc",0,i,"useGetConnectorContextByOrgQuery",0,function(e){let t={...o,...e};return n.useQuery(l,t)},"useGetConnectorContextQuery",0,function(e){let t={...o,...e};return n.useQuery(c,t)}],366541);var u=e.i(951262);let d={},p=t.gql`
    query UserConnectorsPage {
  currentUser {
    id
    __typename
    isSubscribed
    connectorContext {
      __typename
      ...ConnectorContext
      ... on Error {
        message
      }
    }
  }
}
    ${a}`,g=t.gql`
    mutation CreateConnection($input: CreateConnectionInput!) {
  createConnection(input: $input) {
    ... on CreateConnection {
      connectionId
    }
    ... on Error {
      message
    }
  }
}
    `,C=t.gql`
    mutation DeleteConnection($input: DeleteConnectionInput!) {
  deleteConnection(input: $input) {
    ... on DeleteConnection {
      success
    }
  }
}
    `,f=t.gql`
    mutation RequestNewConnector($input: RequestNewConnectorInput!) {
  requestNewConnector(input: $input) {
    ... on RequestNewConnectorResult {
      success
    }
  }
}
    `;e.s(["UserConnectorsPageDocument",0,p,"useCreateConnectionMutation",0,function(e){let t={...d,...e};return u.useMutation(g,t)},"useDeleteConnectionMutation",0,function(e){let t={...d,...e};return u.useMutation(C,t)},"useRequestNewConnectorMutation",0,function(e){let t={...d,...e};return u.useMutation(f,t)},"useUserConnectorsPageQuery",0,function(e){let t={...d,...e};return n.useQuery(p,t)}],335451)},829706,e=>{"use strict";var t=e.i(276385),n=e.i(908796),o=e.i(917736),r=e.i(882848),s=e.i(995691),a=e.i(146432),i=e.i(480028);let c=new Set(["FIGMA","CUSTOM_MCP"]),l=new Set(["BITBUCKET_SOURCE_CONTROL","GITHUB_SOURCE_CONTROL","GITLAB_SOURCE_CONTROL"]),u=new Set(["STRIPE"]),d=new Set(["disconnected","error"]),p=new Set(["YOUTUBE"]),g=[{id:"replit-database",name:"Replit Database",type:"PostgreSQL",icon:(0,t.jsx)(o.default,{size:16,color:i.tokens.blueStronger}),link:"https://docs.replit.com/cloud-services/storage-and-databases/sql-database",pane:{type:"neon"}},{id:"replit-app-storage",name:"Replit App Storage",type:"Object Storage",icon:(0,t.jsx)(a.default,{size:16,color:i.tokens.greenStronger}),link:"https://docs.replit.com/cloud-services/storage-and-databases/object-storage",pane:{type:"objectStorage"}},{id:"replit-auth",name:"Replit Auth",type:"Authentication",icon:(0,t.jsx)(s.default,{size:16,color:i.tokens.orangeStronger}),link:"https://docs.replit.com/replit-workspace/replit-auth#replit-auth",pane:{type:"replitAuth"}},{id:"replit-domains",name:"Replit Domains",type:"Domains",icon:(0,t.jsx)(r.default,{size:16,color:i.tokens.tealStronger}),link:"https://docs.replit.com/cloud-services/deployments/domain-purchasing",pane:{type:"deployments"}}];e.s(["APP_SCOPED_CONNECTORS",0,u,"CONNECTOR_DESCRIPTIONS",0,{AGENTMAIL:"Send, receive, and reply to emails using the AgentMail email inbox API.",AMPLITUDE:"Query analytics data, manage event taxonomy, and trigger project runs in Amplitude",ASHBY:"Access job postings, candidates, and applications from your Ashby ATS",ASANA:"Read tasks and project data from Asana workspaces",SPROUTSOCIAL:"Manage social media profiles, posts, messages, and cases from Sprout Social",BITBUCKET:"Access Bitbucket repositories, users, and organizations from Replit",BITBUCKET_SOURCE_CONTROL:"Sync code to Bitbucket repositories from your Replit apps",GITHUB_SOURCE_CONTROL:"Sync code to GitHub repositories from your Replit apps",GITLAB_SOURCE_CONTROL:"Sync code to GitLab projects from your Replit apps",DATABRICKS_M2M:"Execute SQL queries and manage data workflows in Databricks using a service account",BIGQUERY:"Execute SQL queries on Google BigQuery datasets from your Replit apps",BOX:"Access Box files and folders from Replit",CALENDLY:"View Calendly events and event types",CONFLUENCE:"Read users and groups, create and edit content in Confluence spaces",CLICKUP:"Access tasks, projects, and workflows in ClickUp",DATABRICKS:"Execute SQL queries and manage data workflows in Databricks",DISCORD:"Access Discord guild information and user profiles",DROPBOX:"Access Dropbox files, content, and metadata",ELEVENLABS:"AI voice generation and text-to-speech",HEX:"Run data notebooks, manage projects, and trigger Hex project runs via API",OPENAI:"Access your own OpenAI API key instead of default Replit-managed AI integrations",FACEBOOK:"View Facebook profiles, posts, photos, and manage pages",GITHUB:"Access GitHub repositories, users, and organizations from your Replit apps",GOOGLE_CALENDAR:"Read and write Google Calendar events and settings",GOOGLE_DOCS:"Create, read, and edit Google Docs",GOOGLE_DRIVE:"Access and manage Google Drive files and folders",GOOGLE_MAIL:"Send, receive, and manage Gmail messages",GOOGLE_SHEET:"Read and write data in Google Sheets",GOOGLE_SLIDES:"Create, read, and edit Google Slides presentations",HUBSPOT:"Access HubSpot CRM objects, contacts, and deals from Replit",INSTAGRAM:"Manage Instagram business content, messages, and insights",JIRA:"View users and manage Jira work items and issues",LINEAR:"Create and manage Linear issues, comments, and schedules",MONDAY:"Access Monday.com boards and user information",MOBILE_MAPS:"Access mobile maps and locations from Replit",NOTION:"Read and write to Notion workspaces and pages",ONEDRIVE:"Access and manage OneDrive files and folders",OUTLOOK:"Send and receive emails, manage Outlook calendar events",PLAID:"Access Plaid connected bank accounts and transactions",POSTGRES:"Execute read-only SQL queries on PostgreSQL databases",RESEND:"Send transactional emails using the Resend API",REVENUECAT:"Monetize your mobile apps built on Replit",SALESFORCE:"Access Salesforce CRM data and perform operations via REST API",SEGMENT:"Manage Segment sources, destinations, and tracking plans via the Public API",SENDGRID:"Send transactional emails using the SendGrid API",SHAREPOINT:"Read, write, and manage SharePoint sites and documents",SLACK:"Send messages and interact with Slack workspaces",SLACK_AGENT:"Integrate Slack agent capabilities from Replit",SLACK_AGENT_BUILDER:"Build and manage custom Slack agents",STRIPE:"Connect to Stripe to enable seamless and secure payments for your apps",SNOWFLAKE:"Execute SQL queries on Snowflake data warehouses",SPOTIFY:"Access and manage Spotify playlists and libraries",TODOIST:"Read and write to your Todoist tasks and projects",TWILIO:"Send SMS messages and make voice calls using the Twilio API",YOUTUBE:"Upload and manage YouTube videos, channels, and analytics",ZENDESK:"Access Zendesk users and support tickets from Replit",FIGMA:"Allow Replit Agent to view and rapidly build your designs from Figma",CUSTOM_MCP:"Allows Replit Agent to access external MCP servers",ZOOM:"Access Zoom meetings, users, settings, and webinars with admin privileges",WORKATO:"Trigger Workato recipes and call Workato APIs",X:"Access X posts, users, and search using the X API v2 with pay-per-usage pricing",MICROSOFT_FABRIC:"Access Microsoft Fabric workspaces and resources"},"DISCONNECTED_STATUSES",0,d,"MCP_CONNECTORS",0,c,"REPLIT_MANAGED_SERVICES",0,g,"VERSION_CONTROL_CONNECTORS",0,l,"buildConnectionManagementUrl",0,function(e,t){return`/integrations/${e.toLowerCase()}/apps/${t}`},"isAppScopedConnector",0,e=>u.has(e),"isConnectionHealthy",0,e=>!d.has(e??""),"isHiddenUnlessConnected",0,e=>p.has(e),"isMCPConnector",0,e=>c.has(e),"toConnectorName",0,function(e){if(!e)return null;let t=e.toUpperCase();return Object.values(n.ConnectorName).includes(t)?t:null}])},246549,e=>{"use strict";var t=e.i(389959),n=e.i(335451),o=e.i(366541),r=e.i(829706),s=e.i(151027);let a={};e.s(["useConnectors",0,function(e){let i=e?.skip??!1,{orgId:c}=(0,s.useCurrentUserStoredOrgContext)(),l=!!c,{data:u,loading:d,error:p,refetch:g}=(0,o.useGetConnectorContextQuery)({skip:i||l,context:a}),{data:C,loading:f,error:m,refetch:y}=(0,o.useGetConnectorContextByOrgQuery)({variables:{orgId:c??""},skip:i||!l,context:a}),h=u?.currentUser?.__typename==="CurrentUser"?u?.currentUser?.connectorContext:null,O=C?.currentUser?.__typename==="CurrentUser"&&C?.currentUser?.org?.__typename==="Org"?C?.currentUser?.org?.connectorContext:null,S=l?O:h,b=l?m:p,x=l?f:d,E=l?y:g,[v,{loading:R}]=(0,n.useCreateConnectionMutation)(),A=(0,t.useCallback)(async e=>v({...e,refetchQueries:l?[{query:o.GetConnectorContextByOrgDocument,variables:{orgId:c??""}}]:[{query:o.GetConnectorContextDocument}]}),[v,l,c]),_=S&&(l?"OrgConnectorContext"===S.__typename:"CurrentUserConnectorContext"===S.__typename),I=l?C?.currentUser?.__typename==="CurrentUser"&&C.currentUser.isSubscribed:u?.currentUser?.__typename==="CurrentUser"&&u.currentUser.isSubscribed,U=(0,t.useMemo)(()=>{if(!_||"CurrentUserConnectorContext"!==S.__typename&&"OrgConnectorContext"!==S.__typename)return[];let e=[],t=S.connectorWhitelist??[],n=S.connections??[],o=S.connectorConfigs??[],s=n.filter(e=>(t.includes(e.connectorName)||r.MCP_CONNECTORS.has(e.connectorName))&&!r.APP_SCOPED_CONNECTORS.has(e.connectorName)),a=new Set(s.map(e=>e.connectorName)),i=new Map;o.forEach(e=>{e.connectorName&&e.webhookEvents&&e.webhookEvents.length>0&&i.set(e.connectorName,e.webhookEvents)});let c=o.filter(e=>e.connectorName&&t.includes(e.connectorName)&&!a.has(e.connectorName)&&"CUSTOM_MCP"!==e.connectorName);return s.forEach(t=>{e.push({id:t.connectionId,displayName:t.displayName,iconPath:t.iconPath,connectorName:t.connectorName,connectorType:"connection",type:t.type,webhookEvents:i.get(t.connectorName)})}),c.forEach(t=>{t.connectorName&&e.push({id:t.id,displayName:t.displayName??"Untitled",iconPath:t.iconPath,connectorName:t.connectorName,connectorType:"connectorConfig",type:t.type,webhookEvents:i.get(t.connectorName)})}),e},[_,S]);return b||!_||"CurrentUserConnectorContext"!==S.__typename&&"OrgConnectorContext"!==S.__typename?{token:null,connections:[],connectorConfigs:[],connectorWhitelist:[],slashCommandConnectorItems:[],createConnection:A,loading:x,createConnectionLoading:R,error:b,refetch:E,isSubscribed:I??!1,isOrgContext:l}:{token:S.openIntClientToken,connections:S.connections??[],connectorConfigs:S.connectorConfigs??[],connectorWhitelist:S.connectorWhitelist??[],slashCommandConnectorItems:U,createConnection:A,loading:x,createConnectionLoading:R,error:b,refetch:E,isSubscribed:I??!1,isOrgContext:l}}])},419635,e=>{"use strict";var t=e.i(276385),n=e.i(413974),o=e.i(389959),r=e.i(624071),s=e.i(661594),a=e.i(406664),i=e.i(643484),c=e.i(61732),l=e.i(792789);let u=c.SpecializedView.a,d=(0,o.forwardRef)(function({colorway:e,disabled:o,iconLeft:c,iconRight:d,variant:p="default",size:g="default",stretch:C,text:f,secondaryText:m,href:y,as:h,prefetch:O,replace:S,scroll:b,shallow:x,alignment:E,noNextLink:v,loading:R,dataCy:A,style:_,shrink:I,translate:U,...N},T){let P=(0,i.getTextVariant)(g),w=(0,i.getIconSize)(g),k=(0,a.useCreateInteractive)({variant:"default"===p?void 0:p,colorway:e,loading:R}),D=(0,s.usePressedProps)(),M=(0,t.jsx)(i.ButtonContent,{text:f,secondaryText:m,iconLeft:c,iconRight:d,size:g,iconSize:w,textVariant:P,alignment:E}),L={display:"flex",...k.style,...(0,i.getButtonCssVars)({variant:p,size:g,shrink:I,stretch:C,alignment:E}),..._};if(!o){let e={ref:T,clsx:[l.default.button,k.clsx],style:L,role:"link",translate:U,...(0,r.mergeProps)(D,N)};if(v){if("string"!=typeof y)throw Error("Expected href to be a string");return(0,t.jsx)(u,{dataCy:A,href:y,...e,children:M})}return(0,t.jsx)(n.default,{"data-cy":A,as:h,href:y,prefetch:O,replace:S,scroll:b,shallow:x,...e,children:M})}return(0,t.jsx)(u,{dataCy:A,ref:T,"aria-disabled":o,clsx:[l.default.button,k.clsx],role:"link",style:L,translate:U,...N,children:M})});e.s(["ButtonLink",0,d])},397643,(e,t,n)=>{"use strict";function o(e,t,n,o){return!1}Object.defineProperty(n,"__esModule",{value:!0}),Object.defineProperty(n,"getDomainLocale",{enumerable:!0,get:function(){return o}}),e.r(411410),("function"==typeof n.default||"object"==typeof n.default&&null!==n.default)&&void 0===n.default.__esModule&&(Object.defineProperty(n.default,"__esModule",{value:!0}),Object.assign(n.default,n),t.exports=n.default)},946655,(e,t,n)=>{"use strict";Object.defineProperty(n,"__esModule",{value:!0}),Object.defineProperty(n,"errorOnce",{enumerable:!0,get:function(){return o}});let o=e=>{}},202836,(e,t,n)=>{"use strict";Object.defineProperty(n,"__esModule",{value:!0});var o={default:function(){return v},useLinkStatus:function(){return E}};for(var r in o)Object.defineProperty(n,r,{enumerable:!0,get:o[r]});let s=e.r(887602),a=e.r(478902),i=s._(e.r(389959)),c=e.r(179270),l=e.r(905154),u=e.r(608316),d=e.r(217262),p=e.r(870782),g=e.r(198254),C=e.r(252253),f=e.r(397643),m=e.r(754694),y=e.r(182704);e.r(946655);let h=new Set;function O(e,t,n,o){if(!("u"<typeof window)&&(0,l.isLocalURL)(t)){if(!o.bypassPrefetchedCheck){let r=t+"%"+n+"%"+(void 0!==o.locale?o.locale:"locale"in e?e.locale:void 0);if(h.has(r))return;h.add(r)}e.prefetch(t,n,o).catch(e=>{})}}function S(e){return"string"==typeof e?e:(0,u.formatUrl)(e)}let b=i.default.forwardRef(function(e,t){let n,o,{href:r,as:s,children:u,prefetch:h=null,passHref:b,replace:x,shallow:E,scroll:v,locale:R,onClick:A,onNavigate:_,onMouseEnter:I,onTouchStart:U,legacyBehavior:N=!1,transitionTypes:T,...P}=e;n=u,N&&("string"==typeof n||"number"==typeof n)&&(n=(0,a.jsx)("a",{children:n}));let w=i.default.useContext(g.RouterContext),k=!1!==h,{href:D,as:M}=i.default.useMemo(()=>{if(!w){let e=S(r);return{href:e,as:s?S(s):e}}let[e,t]=(0,c.resolveHref)(w,r,!0);return{href:e,as:s?(0,c.resolveHref)(w,s):t||e}},[w,r,s]),L=i.default.useRef(D),j=i.default.useRef(M);N&&(o=i.default.Children.only(n));let G=N?o&&"object"==typeof o&&o.ref:t,[B,q,$]=(0,C.useIntersection)({rootMargin:"200px"}),F=i.default.useCallback(e=>{(j.current!==M||L.current!==D)&&($(),j.current=M,L.current=D),B(e)},[M,D,$,B]),Q=(0,y.useMergedRef)(F,G);i.default.useEffect(()=>{!w||q&&k&&O(w,D,M,{locale:R})},[M,D,q,R,k,w?.locale,w]);let K={ref:Q,onClick(e){N||"function"!=typeof A||A(e),N&&o.props&&"function"==typeof o.props.onClick&&o.props.onClick(e),!w||e.defaultPrevented||function(e,t,n,o,r,s,a,i,c){let u,{nodeName:d}=e.currentTarget;if(!("A"===d.toUpperCase()&&((u=e.currentTarget.getAttribute("target"))&&"_self"!==u||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||e.nativeEvent&&2===e.nativeEvent.which)||e.currentTarget.hasAttribute("download"))){if(!(0,l.isLocalURL)(n)){r&&(e.preventDefault(),location.replace(n));return}e.preventDefault(),(()=>{if(c){let e=!1;if(c({preventDefault:()=>{e=!0}}),e)return}let e=a??!0;"beforePopState"in t?t[r?"replace":"push"](n,o,{shallow:s,locale:i,scroll:e}):t[r?"replace":"push"](o||n,{scroll:e})})()}}(e,w,D,M,x,E,v,R,_)},onMouseEnter(e){N||"function"!=typeof I||I(e),N&&o.props&&"function"==typeof o.props.onMouseEnter&&o.props.onMouseEnter(e),w&&O(w,D,M,{locale:R,priority:!0,bypassPrefetchedCheck:!0})},onTouchStart:function(e){N||"function"!=typeof U||U(e),N&&o.props&&"function"==typeof o.props.onTouchStart&&o.props.onTouchStart(e),w&&O(w,D,M,{locale:R,priority:!0,bypassPrefetchedCheck:!0})}};if((0,d.isAbsoluteUrl)(M))K.href=M;else if(!N||b||"a"===o.type&&!("href"in o.props)){let e=void 0!==R?R:w?.locale;K.href=w?.isLocaleDomain&&(0,f.getDomainLocale)(M,e,w?.locales,w?.domainLocales)||(0,m.addBasePath)((0,p.addLocale)(M,e,w?.defaultLocale))}return N?i.default.cloneElement(o,K):(0,a.jsx)("a",{...P,...K,children:n})}),x=(0,i.createContext)({pending:!1}),E=()=>(0,i.useContext)(x),v=b;("function"==typeof n.default||"object"==typeof n.default&&null!==n.default)&&void 0===n.default.__esModule&&(Object.defineProperty(n.default,"__esModule",{value:!0}),Object.assign(n.default,n),t.exports=n.default)},413974,(e,t,n)=>{t.exports=e.r(202836)},661594,e=>{"use strict";var t=e.i(729967);e.s(["usePressedProps",0,function(e){let{pressProps:n,isPressed:o}=(0,t.usePress)(e??{});return{...n,"data-pressed":!!o||void 0,"data-rac":""}}])},151027,873054,672220,284693,e=>{"use strict";var t=e.i(276385),n=e.i(488081),o=e.i(389959),r=e.i(973245);let s=r.gql`
    fragment OrgFlagsOrg on Org {
  id
  flags {
    id
    type
    value
  }
}
    `;e.s(["OrgFlagsOrgFragmentDoc",0,s],873054);var a=e.i(304277);e.i(566901);var i=e.i(951262);let c={},l=r.gql`
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
    ${s}`,u=r.gql`
    query CurrentUserOrgContext {
  getUserOrgContext2 {
    ... on Org {
      ...CurrentUserOrg
    }
  }
}
    ${l}`;function d(e){let t={...c,...e};return a.useQuery(u,t)}let p=r.gql`
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
    ${l}`;function g(e){let t={...c,...e};return a.useQuery(p,t)}let C=r.gql`
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
    ${l}`;e.s(["CurrentUserOrgContextDocument",0,u,"CurrentUserOrgContextUpdateOrgContextDocument",0,C,"useCurrentUserOrgContextGetOrgQuery",0,g,"useCurrentUserOrgContextQuery",0,d,"useCurrentUserOrgContextUpdateOrgContextMutation",0,function(e){let t={...c,...e};return i.useMutation(C,t)}],672220),e.i(908796);let f={"flag-sponsorship-bulk-send":"number","flag-org-depl-rules":"boolean","flag-require-git-remote":"boolean","flag-agent-billing-v2-teams":"boolean","flag-org-stack-templates":"boolean","flag-tom-riddle":"boolean","flag-deployments-switch-to-azure":"boolean","flag-experimental-connectors":"string","flag-org-require-security-scan-in-deployment":"boolean","flag-enable-deployment-private-passwords":"boolean","flag-org-custom-mcp-servers":"boolean","flag-org-predefined-mcp-providers":"boolean","flag-org-budgets":"boolean","flag-azure-org-can-use-object-store":"boolean","flag-unified-plans-enterprise":"boolean","flag-self-hosted-git-domains":"boolean","flag-databricks-apps":"boolean","flag-enterprise-deployment-geography-whitelist":"boolean","flag-deployment-geography-selection":"boolean"};function m(e){if(!e||"object"!=typeof e)return!1;let{id:t,type:n,value:o}=e;if(!(t in f))return!1;let r=f[t];return n===r||"number"===r&&"string"===n&&!isNaN(Number(o))}function y(e){return(e.flags||[]).filter(m).reduce((e,{id:t,value:n})=>({...e,[t]:"number"===f[t]?Number(n):n}),{})}e.s(["orgFlags",0,y],284693);var h=e.i(933302);let O=["/evaluations","/import","/integrations","/notifications","/templates","/theme","/@","/~/cli","/grab"],S=(0,o.createContext)(null),b=(0,o.createContext)(null);function x(){let e=(0,o.useContext)(S);if(null===e)throw Error("StoredOrgContextProvider missing!");return e}e.s(["StoredOrgContextProvider",0,function({children:e}){let r=(0,n.useRouter)(),s=r.asPath,a=function(){let e=(0,n.useRouter)().asPath.split("?")[0];if(e.startsWith("/t")){let t=e.split("/");if(t[2])return t[2]}return null}(),i=(0,h.useSyncStatsigOrgContext)(),c=null!=a,l=!c&&O.some(e=>s.startsWith(e)),u=d({skip:"/replEnvironmentDesktop"===r.pathname||"/replEnvironmentMobile"===r.pathname||!l}),p=u.data?.getUserOrgContext2?.__typename==="Org"?u.data.getUserOrgContext2:null,C=g({skip:!c,variables:{orgSlug:a??""}}),f=C.data?.currentUser?.org?.__typename==="Org"?C.data.currentUser.org:null,m=l?u.loading:C.loading,x=c?f:l?p:null;i(x?.id,x?.dealContext?.dealType);let[E,v]=(0,o.useState)({orgId:x?.id,orgSlug:x?.slug,orgRole:x?.currentUserRole??void 0,orgDealContext:x?.dealContext??void 0});(0,o.useEffect)(()=>{m||v({orgId:x?.id,orgSlug:x?.slug,orgRole:x?.currentUserRole??void 0,orgDealContext:x?.dealContext??void 0})},[x,m]);let R=(0,o.useCallback)(e=>v(e),[]),A=(0,o.useMemo)(()=>x?y(x):{},[x]);return(0,t.jsx)(b.Provider,{value:R,children:(0,t.jsx)(S.Provider,{value:{flags:A,orgId:E.orgId,orgSlug:E.orgSlug,orgRole:E.orgRole,orgDealContext:E.orgDealContext,loading:m},children:e})})},"getOrgTrackingContext",0,e=>e?`Org:${e.id}`:"Personal","useCurrentUserStoredOrgContext",0,x,"useIsCurrentOrgEnterprise",0,function(){let e=x();return e.orgDealContext?.dealType==="enterprise"||e.orgDealContext?.dealType==="enterprise_trial"},"useSetOptimisticOrg",0,function(){let e=(0,o.useContext)(b);if(null===e)throw Error("StoredOrgContextProvider missing!");return e}],151027)},843400,e=>{e.v({modalContent:"EmbedModal-module__oAShma__modalContent",overlay:"EmbedModal-module__oAShma__overlay",overlayTopAligned:"EmbedModal-module__oAShma__overlayTopAligned"})},554370,e=>{"use strict";var t=e.i(276385),n=e.i(389959),o=e.i(486597),r=e.i(624071),s=e.i(342942),a=e.i(739261),i=e.i(969407),c=e.i(918542),l=e.i(691636),u=e.i(61732),d=e.i(843400);e.s(["EmbedModal",0,function({isOpen:e,onRequestClose:p,children:g,maxWidth:C=800,maxHeight:f,centered:m=!0,zIndex:y,className:h,portalContainer:O}){let S=(0,i.useIsSSR)(),b=(0,n.useRef)(null),x=(0,o.useOverlayTriggerState)({isOpen:e,onOpenChange:e=>{e||p()}}),{modalProps:E,underlayProps:v}=(0,c.useModalOverlay)({isDismissable:!0,isKeyboardDismissDisabled:!1,shouldCloseOnInteractOutside:e=>!(e.tagName.toLowerCase().includes("1password")||e.tagName.toLowerCase().includes("com-1password")||e.hasAttribute("data-op-target")||e.hasAttribute("data-op-id")||Array.from(e.attributes).some(e=>e.name.startsWith("data-1p-"))||e.className?.toString().includes("op-")||null!==e.closest('[class*="1password"]')||null!==e.closest('[class*="op-"]')||null!==e.closest("[data-op-target]"))},x,b),{dialogProps:R}=(0,a.useDialog)({"aria-label":"Embed content"},b);return((0,n.useEffect)(()=>{let t=t=>{"Escape"===t.key&&e&&p()};return document.addEventListener("keydown",t),()=>document.removeEventListener("keydown",t)},[e,p]),S||!e)?null:(0,t.jsx)(s.Overlay,{portalContainer:O??document.body,children:(0,t.jsx)("div",{...v,className:m?d.default.overlay:`${d.default.overlay} ${d.default.overlayTopAligned}`,style:{zIndex:y??l.DefaultModalZIndex},children:(0,t.jsx)("div",{...(0,r.mergeProps)(E,R),ref:b,className:`${d.default.modalContent} ${h||""}`,style:{maxWidth:C,maxHeight:f??"calc(100vh - 64px)"},children:(0,t.jsx)(u.View,{children:g})})})})}])}]);

//# debugId=a2a6e69b-ab4e-f148-9e65-45b7607ec356
//# sourceMappingURL=0y2-wskbg2773.js.map
