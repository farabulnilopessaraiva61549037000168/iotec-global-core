;!function(){try { var e="undefined"!=typeof globalThis?globalThis:"undefined"!=typeof global?global:"undefined"!=typeof window?window:"undefined"!=typeof self?self:{},n=(new e.Error).stack;n&&((e._debugIds|| (e._debugIds={}))[n]="3cd09c20-6951-12e1-eced-3e878a022d72")}catch(e){}}();
(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,413325,e=>{e.v({buttonGroupContainer:"List-module__a4KWka__buttonGroupContainer",compact:"List-module__a4KWka__compact",emptyState:"List-module__a4KWka__emptyState",emptyStateContainer:"List-module__a4KWka__emptyStateContainer",list:"List-module__a4KWka__list",loadMoreContainer:"List-module__a4KWka__loadMoreContainer",textCenter:"List-module__a4KWka__textCenter"})},638046,e=>{e.v({count:"NotificationsItem-module__00pi2G__count"})},286093,736372,556278,566032,70219,246613,13465,e=>{"use strict";var t=e.i(276385),i=e.i(389959),o=e.i(973245);let n=o.gql`
    fragment NotificationItemCreator on User {
  id
  image
  username
  fullName
  url
}
    `,a=o.gql`
    fragment NotificationItemRepliedToPostNotification on RepliedToPostNotification {
  id
  text
  url
  timeCreated
  seen
  creator {
    id
    ...NotificationItemCreator
  }
}
    ${n}`,r=o.gql`
    fragment NotificationItemRepliedToCommentNotification on RepliedToCommentNotification {
  id
  text
  url
  timeCreated
  seen
  creator {
    id
    ...NotificationItemCreator
  }
}
    ${n}`,s=o.gql`
    fragment NotificationItemMentionedInPostNotification on MentionedInPostNotification {
  id
  text
  url
  timeCreated
  seen
  creator {
    id
    ...NotificationItemCreator
  }
}
    ${n}`,c=o.gql`
    fragment NotificationItemMentionedInCommentNotification on MentionedInCommentNotification {
  id
  text
  url
  timeCreated
  seen
  creator {
    id
    ...NotificationItemCreator
  }
}
    ${n}`,l=o.gql`
    fragment NotificationItemAnswerAcceptedNotification on AnswerAcceptedNotification {
  id
  text
  url
  timeCreated
  seen
  creator {
    id
    ...NotificationItemCreator
  }
}
    ${n}`,m=o.gql`
    fragment NotificationItemMultiplayerJoinedEmailNotification on MultiplayerJoinedEmailNotification {
  id
  text
  url
  timeCreated
  seen
  creator {
    id
    ...NotificationItemCreator
  }
}
    ${n}`,d=o.gql`
    fragment NotificationItemMultiplayerJoinedLinkNotification on MultiplayerJoinedLinkNotification {
  id
  text
  url
  timeCreated
  seen
  creator {
    id
    ...NotificationItemCreator
  }
}
    ${n}`,u=o.gql`
    fragment NotificationItemMultiplayerInvitedNotification on MultiplayerInvitedNotification {
  id
  text
  url
  timeCreated
  seen
  creator {
    id
    ...NotificationItemCreator
  }
}
    ${n}`,f=o.gql`
    fragment NotificationItemMultiplayerOverlimitNotification on MultiplayerOverlimitNotification {
  id
  text
  url
  timeCreated
  seen
  creator {
    id
    ...NotificationItemCreator
  }
}
    ${n}`,p=o.gql`
    fragment NotificationItemWarningNotification on WarningNotification {
  id
  text
  url
  timeCreated
  seen
}
    `,x=o.gql`
    fragment NotificationItemTeamInvite on TeamInvite {
  id
  team {
    id
    displayName
    username
  }
}
    `,N=o.gql`
    fragment NotificationItemTeamInviteNotification on TeamInviteNotification {
  id
  text
  url
  timeCreated
  seen
  invite {
    id
    ...NotificationItemTeamInvite
  }
}
    ${x}`,g=o.gql`
    fragment NotificationItemTeamOrganizationInvite on TeamOrganizationInvite {
  id
  organization {
    id
    name
  }
}
    `,h=o.gql`
    fragment NotificationItemTeamOrganizationInviteNotification on TeamOrganizationInviteNotification {
  id
  text
  url
  timeCreated
  seen
  invite {
    id
    ...NotificationItemTeamOrganizationInvite
  }
}
    ${g}`,C=o.gql`
    fragment NotificationTeamTemplateSubmittedNotification on TeamTemplateSubmittedNotification {
  id
  text
  url
  timeCreated
  seen
  repl {
    id
    url
  }
}
    `,j=o.gql`
    fragment NotificationTeamTemplateReviewedStatusNotification on TeamTemplateReviewedStatusNotification {
  id
  text
  url
  timeCreated
  seen
  repl {
    id
    url
  }
}
    `,I=o.gql`
    fragment NotificationReplCommentCreatedNotification on ReplCommentCreatedNotification {
  id
  url
  timeCreated
  seen
  creator {
    id
    ...NotificationItemCreator
  }
}
    ${n}`,v=o.gql`
    fragment NotificationReplCommentReplyCreatedNotification on ReplCommentReplyCreatedNotification {
  id
  timeCreated
  seen
  creator {
    id
    ...NotificationItemCreator
  }
}
    ${n}`,y=o.gql`
    fragment NotificationReplCommentMentionNotification on ReplCommentMentionNotification {
  id
  timeCreated
  seen
  creator {
    id
    ...NotificationItemCreator
  }
}
    ${n}`,w=o.gql`
    fragment NotificationItemNewFollower on NewFollowerNotification {
  id
  timeCreated
  seen
  url
  creator {
    ...NotificationItemCreator
  }
}
    ${n}`,_=o.gql`
    fragment BasicNotificationItemNotification on BasicNotification {
  id
  text
  url
  timeCreated
  seen
  context
}
    `,T=o.gql`
    fragment NotificationItemEgressLimitNotification on EgressLimitNotification {
  id
  url
  timeCreated
  seen
  variant
  limitGib
  percentage
}
    `,k=o.gql`
    fragment NotificationItemOrgUpgradeRequestReviewedNotification on OrgUpgradeRequestReviewedNotification {
  id
  timeCreated
  seen
  url
  creator {
    ...NotificationItemCreator
  }
  isAccepted
  orgId
}
    ${n}`;var R=e.i(304277);e.i(566901);let M={},b=o.gql`
    fragment NotificationItems on Notification {
  ... on BasicNotification {
    id
    ...BasicNotificationItemNotification
  }
  ... on MentionedInPostNotification {
    id
    ...NotificationItemMentionedInPostNotification
  }
  ... on RepliedToPostNotification {
    id
    ...NotificationItemRepliedToPostNotification
  }
  ... on MentionedInCommentNotification {
    id
    ...NotificationItemMentionedInCommentNotification
  }
  ... on RepliedToCommentNotification {
    id
    ...NotificationItemRepliedToCommentNotification
  }
  ... on AnswerAcceptedNotification {
    id
    ...NotificationItemAnswerAcceptedNotification
  }
  ... on MultiplayerInvitedNotification {
    id
    ...NotificationItemMultiplayerInvitedNotification
  }
  ... on MultiplayerJoinedEmailNotification {
    id
    ...NotificationItemMultiplayerJoinedEmailNotification
  }
  ... on MultiplayerJoinedLinkNotification {
    id
    ...NotificationItemMultiplayerJoinedLinkNotification
  }
  ... on MultiplayerOverlimitNotification {
    id
    ...NotificationItemMultiplayerOverlimitNotification
  }
  ... on WarningNotification {
    id
    ...NotificationItemWarningNotification
  }
  ... on TeamInviteNotification {
    id
    ...NotificationItemTeamInviteNotification
  }
  ... on TeamOrganizationInviteNotification {
    id
    ...NotificationItemTeamOrganizationInviteNotification
  }
  ... on TeamTemplateSubmittedNotification {
    id
    ...NotificationTeamTemplateSubmittedNotification
  }
  ... on TeamTemplateReviewedStatusNotification {
    id
    ...NotificationTeamTemplateReviewedStatusNotification
  }
  ... on ReplCommentCreatedNotification {
    id
    ...NotificationReplCommentCreatedNotification
  }
  ... on ReplCommentReplyCreatedNotification {
    id
    ...NotificationReplCommentReplyCreatedNotification
  }
  ... on ReplCommentMentionNotification {
    id
    ...NotificationReplCommentMentionNotification
  }
  ... on NewFollowerNotification {
    id
    ...NotificationItemNewFollower
  }
  ... on OrgUpgradeRequestReviewedNotification {
    id
    ...NotificationItemOrgUpgradeRequestReviewedNotification
  }
  ... on EgressLimitNotification {
    id
    ...NotificationItemEgressLimitNotification
  }
  ... on OrgUpgradeRequestReviewedNotification {
    id
    ...NotificationItemOrgUpgradeRequestReviewedNotification
  }
}
    ${_}
${s}
${a}
${c}
${r}
${l}
${u}
${m}
${d}
${f}
${p}
${N}
${h}
${C}
${j}
${I}
${v}
${y}
${w}
${k}
${T}`,L=o.gql`
    query notifications($after: String, $count: Int, $seen: Boolean) {
  currentUser {
    id
  }
  notifications(after: $after, count: $count, seen: $seen) {
    items {
      ...NotificationItems
    }
    pageInfo {
      nextCursor
    }
  }
}
    ${b}`;var S=e.i(951262);let A={},O=o.gql`
    mutation MarkAllNotificationsAsSeen {
  markAllNotificationsAsSeen {
    id
    notificationCount
  }
}
    `;var $=e.i(183035),q=e.i(269848),P=e.i(413974),E=e.i(927600),U=e.i(415541),W=e.i(709485),z=e.i(480028),V=e.i(462229),B=e.i(723517),D=e.i(691636);let F=(0,V.cssRecord)({root:[D.rcss.display.flex,D.rcss.align.center,D.rcss.p(12),{'&[data-has-link="true"]':[{pointerEvents:"none","a, button":{pointerEvents:"all"}}],'&[data-last-item="true"]':[D.rcss.border({width:1,color:z.tokens.outlineDimmest,direction:"bottom"})]}],notificationLinkWrapper:[[{borderWidth:0,":nth-last-child(2)>a":{borderBottomLeftRadius:z.tokens.space8,borderBottomRightRadius:z.tokens.space8,"::after":{borderBottomLeftRadius:z.tokens.space8,borderBottomRightRadius:z.tokens.space8}}}]],notificationLink:[B.interactive.listItem,D.rcss.color.foregroundDefault,D.rcss.display.block,D.rcss.focusRingOnAfter,D.rcss.position.relative,{":focus-visible":{boxShadow:"none !important"},"::after":{content:'""',position:"absolute",top:0,right:0,bottom:0,left:0,display:"block",zIndex:1}}],content:[D.rcss.flex.grow(1),D.rcss.pr(12)],indicatorLink:[D.rcss.display.flex,D.rcss.align.center],indicator:[D.rcss.width(6),D.rcss.height(6),D.rcss.backgroundColor.blueStronger,D.rcss.borderRadius("full"),D.rcss.mr(2)]}),G=({condition:e,children:t,wrap:o})=>e?(0,i.cloneElement)(o(t)):t;function H({children:e,seen:i,href:o,as:n,isLastItem:a=!1}){let r=!!(o||n);return(0,t.jsx)(G,{condition:r,wrap:e=>(0,t.jsxs)("div",{css:F.notificationLinkWrapper,children:[n&&o?(0,t.jsx)(P.default,{as:n,href:o,css:F.notificationLink,children:e}):null,!n&&o&&"object"==typeof o?(0,t.jsx)(P.default,{href:o,css:F.notificationLink,children:e}):null,n||"string"!=typeof o?null:(0,t.jsx)("a",{css:F.notificationLink,href:o,children:e})]}),children:(0,t.jsxs)("div",{onClick:()=>{r&&(0,U.track)(W.events.NOTIFICATION_ITEM_CLICKED,{seen:i})},css:F.root,"data-has-link":r,"data-last-item":a,children:[(0,t.jsx)("div",{css:F.content,children:e}),r?(0,t.jsxs)("div",{css:F.indicatorLink,children:[!i&&(0,t.jsx)("div",{css:F.indicator}),(0,t.jsx)(E.default,{color:z.tokens.foregroundDimmest})]}):null]})})}var K=e.i(192915),J=e.i(967629),Y=e.i(825419),Q=e.i(8047),X=e.i(472499),Z=e.i(61732);let ee=(0,J.css)([D.rcss.position.relative,D.rcss.display.flex,{flex:"1 1 auto"}]),et=(0,V.cssRecord)({content:ee,contentContainer:[ee,D.rcss.rowWithGap(12),D.rcss.align.center],itemText:[D.rcss.pb(4),{overflowWrap:"break-word"}],itemTextNewFollowerWrapper:[D.rcss.display.flex,D.rcss.flex.column],usernameLink:[D.rcss.borderRadius(4),D.rcss.focusRing,{":focus":{outlineOffset:0}}],userAvatarLink:[D.rcss.width(32),D.rcss.height(32),D.rcss.minWidth(32),D.rcss.minHeight(32),D.rcss.borderRadius(16),D.rcss.focusRing,{":focus":{outlineOffset:0}}]}),ei=({seen:e,url:i,as:o,href:n,text:a,timeCreated:r,creator:s,invite:c,orgInvite:l,isLastItem:m=!1,...d})=>{let u,f;return i&&((u=new URL("/"===i[0]?`https://replit.com${i}`:i)).searchParams.set("from","notifications"),f=(i.startsWith("http")&&"https:"===u.protocol?u.protocol+"//"+u.hostname:"")+u.pathname+u.search+u.hash),(0,t.jsx)(H,{seen:e,compact:d.compact,isLastItem:m,as:o,href:n||f,children:(0,t.jsxs)("div",{css:et.contentContainer,children:[s?(0,t.jsx)(P.default,{...(0,K.userLinkProps)(s),css:et.userAvatarLink,children:(0,t.jsx)(Y.Avatar,{size:32,src:s.image,username:s.username,fullName:s.fullName})}):null,(0,t.jsxs)(Z.View,{shrink:!0,children:[(0,t.jsxs)("div",{css:et.itemText,children:[s?(0,t.jsx)(P.default,{...(0,K.userLinkProps)(s),css:et.usernameLink,children:s.username}):null," ",a,c?(0,t.jsx)(t.Fragment,{children:` ${c.team.displayName}. Click here to join`}):null,l?(0,t.jsx)(t.Fragment,{children:` the ${l.organization.name} workspace. Click here to join`}):null]}),(0,t.jsx)(Q.Text,{variant:"small",color:"dimmer",multiline:!1,children:(0,t.jsx)(X.Timestamp,{date:r})})]})]})})},eo=({notification:e,isLastItem:i,setAsSeen:o,...n})=>{if("ReplCommentCreatedNotification"===e.__typename||"ReplCommentReplyCreatedNotification"===e.__typename||"ReplCommentMentionNotification"===e.__typename){let a={ReplCommentCreatedNotification:"commented on your repl",ReplCommentReplyCreatedNotification:"replied to your comment on your repl",ReplCommentMentionNotification:"mentioned you in your repl"}[e.__typename];return(0,t.jsx)(ei,{isLastItem:i,text:a||void 0,seen:o||e.seen,compact:n.compact,timeCreated:e.timeCreated,creator:e.creator||void 0})}if("BasicNotification"===e.__typename)return(0,t.jsx)(ei,{isLastItem:i,text:e.text||void 0,seen:o||e.seen,compact:n.compact,timeCreated:e.timeCreated,url:e.url});if("MentionedInPostNotification"===e.__typename)return(0,t.jsx)(ei,{isLastItem:i,text:"mentioned you in their post",creator:e.creator||void 0,seen:o||e.seen,compact:n.compact,timeCreated:e.timeCreated,url:e.url});if("MentionedInCommentNotification"===e.__typename)return(0,t.jsx)(ei,{isLastItem:i,text:"mentioned you in their comment",creator:e.creator||void 0,seen:o||e.seen,compact:n.compact,timeCreated:e.timeCreated,url:e.url});if("RepliedToPostNotification"===e.__typename)return(0,t.jsx)(ei,{isLastItem:i,text:"replied to your post",creator:e.creator||void 0,seen:o||e.seen,compact:n.compact,timeCreated:e.timeCreated,url:e.url});if("RepliedToCommentNotification"===e.__typename)return(0,t.jsx)(ei,{isLastItem:i,text:"replied to your comment",creator:e.creator||void 0,seen:o||e.seen,compact:n.compact,timeCreated:e.timeCreated,url:e.url});if("AnswerAcceptedNotification"===e.__typename)return(0,t.jsx)(ei,{isLastItem:i,text:"accepted your answer (you earned 5 cycles!)",creator:e.creator||void 0,seen:o||e.seen,compact:n.compact,timeCreated:e.timeCreated,url:e.url});if("WarningNotification"===e.__typename)return(0,t.jsx)(ei,{isLastItem:i,text:"You have been warned by a moderator.  Click here to learn more.",seen:o||e.seen,compact:n.compact,timeCreated:e.timeCreated,url:e.url});if("TeamInviteNotification"===e.__typename)return(0,t.jsx)(ei,{isLastItem:i,text:"You have been invited to join",invite:e.invite||void 0,seen:o||e.seen,compact:n.compact,timeCreated:e.timeCreated,url:e.url});if("TeamOrganizationInviteNotification"===e.__typename)return(0,t.jsx)(ei,{isLastItem:i,text:"You have been invited to join",orgInvite:e.invite||void 0,seen:o||e.seen,compact:n.compact,timeCreated:e.timeCreated,url:e.url});if("MultiplayerJoinedEmailNotification"===e.__typename||"MultiplayerJoinedLinkNotification"===e.__typename||"MultiplayerInvitedNotification"===e.__typename||"MultiplayerOverlimitNotification"===e.__typename)return(0,t.jsx)(ei,{isLastItem:i,text:e.text?e.text.split(" ").slice(1).join(" "):"",creator:e.creator||void 0,seen:o||e.seen,compact:n.compact,timeCreated:e.timeCreated,url:e.url});if("TeamTemplateSubmittedNotification"===e.__typename||"TeamTemplateReviewedStatusNotification"===e.__typename)return(0,t.jsx)(ei,{isLastItem:i,text:e.text,seen:o||e.seen,compact:n.compact,timeCreated:e.timeCreated,url:e.repl?.url||e.url});if("NewFollowerNotification"===e.__typename){let a=e.creator?(0,K.userLinkProps)(e.creator):null;return(0,t.jsx)(H,{seen:o||e.seen,compact:n.compact,as:a?.as,href:a?.href,isLastItem:i,children:(0,t.jsxs)("div",{css:et.contentContainer,children:[(0,t.jsx)(Y.Avatar,{size:32,src:e.creator?.image??null,username:e.creator?.username??"",fullName:e.creator?.fullName}),(0,t.jsx)("div",{css:et.content,children:(0,t.jsx)("div",{css:et.itemTextNewFollowerWrapper,children:(0,t.jsxs)("div",{css:et.itemText,children:[(0,t.jsxs)("div",{children:[e.creator?(0,t.jsx)(P.default,{...(0,K.userLinkProps)(e.creator),children:e.creator.username}):"[deleted]"," started following you"]}),(0,t.jsx)(Q.Text,{variant:"small",color:"dimmer",multiline:!1,children:(0,t.jsx)(X.Timestamp,{date:e.timeCreated})})]})})})]})})}return"OrgUpgradeRequestReviewedNotification"===e.__typename?(0,t.jsx)(ei,{creator:e.creator||void 0,isLastItem:i,text:e.isAccepted?"approved your request to join the workspace":"rejected your request to join the workspace",seen:o||e.seen,compact:n.compact,timeCreated:e.timeCreated,url:e.url}):"EgressLimitNotification"===e.__typename?(0,t.jsx)(ei,{creator:void 0,isLastItem:i,text:"egress_reached_limit"===e.variant?"You have reached your data transfer limit for the month. Your Apps' data transfer is being throttled, and will be shut off. Upgrade your plan or purchase additional data transfer with Cycles to resume normal speeds.":`You have used ${e.percentage}% of your monthly data transfer limit. If you reach the limit, your Apps data transfer will be throttled and eventually shut off. Upgrade your plan or purchase additional data transfer with Cycles to prevent disruptions to your Apps.`,seen:o||e.seen,compact:n.compact,timeCreated:e.timeCreated,url:e.url}):null},en={},ea=o.gql`
    mutation MarkNotificationsAsSeen($ids: [Int!]) {
  markNotificationsAsSeen(ids: $ids)
}
    `;var er=e.i(980224);let es=e=>{var t;let o,[n,a]=(0,i.useState)([]),{count:r,setUnreadCount:s}=(0,er.default)(),c=e.notificationIds.filter(e=>-1===n.indexOf(e)),[l,{data:m}]=(t={variables:{ids:c}},o={...en,...t},S.useMutation(ea,o));return(0,i.useEffect)(()=>{0!==c.length&&(a([...n,...c]),l())},[c,l]),(0,i.useEffect)(()=>{m?.markNotificationsAsSeen&&s(Math.max(0,r-m.markNotificationsAsSeen))},[m,s]),null};var ec=e.i(766299),el=e.i(643484),em=e.i(449525),ed=e.i(413325);e.s(["default",0,e=>{var o,n;let a,r,[s,c]=(0,i.useState)(!0),{count:l}=(0,er.default)(),[m,d]=(0,i.useState)(!1),{data:u,loading:f,fetchMore:p}=(o={fetchPolicy:"cache-and-network",ssr:!1,notifyOnNetworkStatusChange:!0,variables:{...e.count?{count:e.count}:{},...s?{seen:!1}:{}}},a={...M,...o},R.useQuery(L,a)),x=(u?.notifications?.items??[]).filter(e=>"AnnotationNotification"!==e.__typename&&"ThreadNotification"!==e.__typename),[N]=(n={onCompleted(){d(!1)},optimisticResponse:{__typename:"RootMutationType",markAllNotificationsAsSeen:{__typename:"CurrentUser",id:u?.currentUser?.id,notificationCount:0}}},r={...A,...n},S.useMutation(O,r)),g=(0,ec.useIdSeed)();return(0,t.jsxs)(t.Fragment,{children:[(0,t.jsxs)(Z.View,{row:!0,gap:16,justify:"space-between",clsx:[ed.default.list,{[ed.default.compact]:e.compact}],children:[(0,t.jsx)("div",{clsx:[ed.default.buttonGroupContainer,{[ed.default.compact]:e.compact&&l>0}],children:(0,t.jsxs)(em.ButtonGroup,{name:g("visibility"),value:s.toString(),primary:!0,onChange:()=>c(!s),row:!0,stretch:!0,children:[(0,t.jsx)(em.ButtonGroupItem,{id:g("true"),value:"true",text:"Unread"}),(0,t.jsx)(em.ButtonGroupItem,{id:g("false"),value:"false",text:"All"})]})}),l>0&&(0,t.jsx)(el.Button,{text:m?"Marking all...":"Mark as read",disabled:f,iconLeft:(0,t.jsx)($.default,{}),stretch:!0,onClick:()=>{d(!0),N()}})]}),(0,t.jsxs)(Z.View,{children:[!f||u&&u.notifications?null:(0,t.jsx)(Z.View,{p:64,align:"center",children:(0,t.jsx)(q.default,{})}),0===x.length&&(0,t.jsx)("div",{clsx:[ed.default.emptyStateContainer,{[ed.default.compact]:e.compact}],children:(0,t.jsx)(Z.View,{clsx:[ed.default.emptyState,{[ed.default.compact]:e.compact}],children:(0,t.jsx)(Q.Text,{variant:"text",color:"dimmer",multiline:!1,clsx:ed.default.textCenter,children:s?"You're all caught up!":"No notifications"})})}),x.length?(0,t.jsxs)(t.Fragment,{children:[x.map((i,o)=>(0,t.jsx)(eo,{compact:e.compact,notification:i,isLastItem:o===x.length-1,setAsSeen:!0},i.id)),e.markAsSeen&&(0,t.jsx)(es,{notificationIds:x.filter(e=>"seen"in e&&!e.seen).map(e=>e.id)})]}):null,e.loadMore&&u?.notifications.pageInfo.nextCursor?(0,t.jsx)("div",{clsx:[ed.default.loadMoreContainer,{[ed.default.compact]:e.compact}],children:(0,t.jsx)(el.Button,{text:f?"Loading...":"Load more",onClick:()=>{f||p({variables:{after:u&&u.notifications&&!s?u.notifications.pageInfo.nextCursor:null},updateQuery:(e,t)=>{if(!t||!t.fetchMoreResult)return e;let{fetchMoreResult:i}=t,o=e?e.notifications.items:[],n={...i};return n.notifications.items=[...o,...i.notifications.items],n}})},disabled:f})}):null]})]})}],286093);var eu=e.i(488081),ef=e.i(908796),ep=e.i(712903),ex=e.i(255701),eN=e.i(195206),eg=e.i(334028),eh=e.i(177037),eC=e.i(596139),ej=e.i(294827),eI=e.i(776065),ev=e.i(926233),ey=e.i(983420),ew=e.i(295231);function e_({right:e,label:i,...o}){return(0,t.jsxs)(ew.BaseMenuItem,{textValue:i,...o,children:[(0,t.jsxs)(Z.View,{gap:6,pl:2,row:!0,align:"center",grow:!0,shrink:!0,children:[(0,t.jsx)(ey.IconProvider,{size:16,children:o.icon}),(0,t.jsx)(ew.MenuItemLabel,{children:i})]}),e??null]})}var eT=e.i(648880),ek=e.i(919073),eR=e.i(638046);function eM({count:e,onAction:i}){return(0,t.jsx)(ew.BaseMenuItem,{textValue:"Notifications",onAction:i,children:(0,t.jsxs)(Z.View,{align:"center",row:!0,gap:6,justify:"space-between",grow:!0,shrink:!0,children:[(0,t.jsxs)(Z.View,{align:"center",grow:!0,shrink:!0,row:!0,gap:6,children:[(0,t.jsx)(eT.default,{}),(0,t.jsx)(Q.Text,{children:"Notifications"})]}),e?(0,t.jsx)(ek.ShadesSurface,{clsx:eR.default.count,colorShade:"themeError",align:"center",justify:"center",children:(0,t.jsx)(Q.Text,{variant:"small",children:e})}):null]})})}e.s(["AccountItems",0,function({currentUser:e,setActiveModal:i,notificationCount:o,isUnifiedPlanEnabled:n,onClose:a}){let r=(0,eu.useRouter)(),s=(0,K.userLinkProps)(e),{shouldHidePersonalWorkspace:c}=(0,ej.usePersonalWorkspacesDisabled)();return(0,t.jsxs)(t.Fragment,{children:[n?(0,t.jsx)(ew.MenuItem,{label:"Settings",icon:(0,t.jsx)(ex.default,{}),onAction:()=>{(0,eI.updatePathWithQueryParams)({router:r,params:[{mode:"add",key:ev.SETTINGS_SHOW_PARAM,value:"true"}]}),a?.()}}):(0,t.jsx)(e_,{label:"Account",as:"/account",href:"/account",dataCy:"avatar-dropdown-account-link",icon:e.isMemberOfAnyOrg?(0,t.jsx)(ex.default,{}):(0,t.jsx)(Y.Avatar,{size:16,src:e.image,username:e.username,fullName:e.fullName}),right:e.userSubscriptionType===ef.UserSubscriptionTypeEnum.HackerPro?(0,t.jsxs)(Z.View,{row:!0,align:"center",gap:4,children:[(0,t.jsx)(ep.default,{size:12,color:eh.brandOrange}),(0,t.jsx)(Q.Text,{variant:"small",color:"dimmer",translate:"no",children:eC.corePlanName})]}):null}),c||n?null:(0,t.jsx)(ew.MenuItem,{label:"Profile",as:s.as,href:s.href,dataCy:"avatar-dropdown-account-link",icon:(0,t.jsx)(eg.default,{})}),(0,t.jsx)(eM,{count:o,onAction:()=>{i("notifications")}}),(0,t.jsx)(ew.Separator,{}),(0,t.jsx)(ew.MenuItem,{label:"CLUI",as:"/~/cli",href:"/~/cli",icon:(0,t.jsx)(eN.default,{})}),(0,t.jsx)(ew.Separator,{})]})}],736372),e.i(155865);var eb=e.i(320216);e.s(["DevCopyUsernameItem",0,function({currentUser:e}){let{showConfirm:i}=(0,eb.default)();return(0,t.jsx)(t.Fragment,{children:null})}],556278);var eL=e.i(625251),eS=e.i(787527),eA=e.i(399245),eO=e.i(222878),e$=e.i(735362),eq=e.i(761201),eP=e.i(519979);function eE(){return(0,t.jsx)(ew.MenuItem,{icon:(0,t.jsx)(eP.default,{}),label:"Status",href:"https://status.replit.com"})}var eU=e.i(773222);e.s(["HelpItem",0,function({setActiveModal:e,children:i}){return(0,t.jsx)(t.Fragment,{children:(0,t.jsxs)(eL.SubmenuTrigger,{children:[(0,t.jsx)(ew.BaseMenuItem,{textValue:"Help",children:(0,t.jsxs)(Z.View,{align:"center",row:!0,gap:6,justify:"space-between",grow:!0,shrink:!0,children:[(0,t.jsxs)(Z.View,{align:"center",grow:!0,shrink:!0,row:!0,gap:6,children:[(0,t.jsx)(eO.default,{}),(0,t.jsx)(Q.Text,{children:"Help"})]}),(0,t.jsx)(E.default,{size:12})]})}),(0,t.jsx)(eU.RawPopover,{offset:4,children:(0,t.jsx)(Z.View,{p:4,children:(0,t.jsxs)(ew.Menu,{"aria-label":"Help",children:[(0,t.jsx)(eE,{}),(0,t.jsx)(ew.MenuItem,{label:"Get help",icon:(0,t.jsx)(eO.default,{size:16}),onAction:()=>{e("support"),(0,U.track)(W.events.HELP_FORM_OPENED,{type:"New Help Form"})}}),(0,t.jsx)(ew.MenuItem,{icon:(0,t.jsx)(eA.default,{}),label:"Community Hub",href:eq.COMMUNITY_URL}),(0,t.jsx)(ew.MenuItem,{icon:(0,t.jsx)(e$.default,{}),label:"View updates",href:eq.LINKS_DOCS.CHANGELOG,onAction:()=>{(0,U.track)(W.events.CHANGELOG_OPENED)}}),(0,t.jsx)(ew.MenuItem,{icon:(0,t.jsx)(eS.default,{}),label:"Read the docs",href:eq.LINKS_DOCS.HOME,onAction:()=>{(0,U.track)(W.events.DOCS_OPENED,{source:"help_menu"})}}),i]})})})]})})}],566032);var eW=e.i(442121),ez=e.i(98346),eV=e.i(443197);e.s(["LogoutItem",0,function(){let e=(0,eW.useApolloClient)();return(0,t.jsx)(ew.MenuItem,{label:"Log out",icon:(0,t.jsx)(ez.default,{}),onAction:async()=>{await (0,eV.signOut)(e),window.location.href="/logout"}})}],70219);var eB=e.i(151027),eD=e.i(648552),eF=e.i(448942),eG=e.i(276887);e.s(["TeamsItem",0,function({currentUser:e}){let i=(0,eB.useCurrentUserStoredOrgContext)(),{loading:o}=i,n=(0,eD.useOrgSwitcher)(),{shouldHidePersonalWorkspace:a}=(0,ej.usePersonalWorkspacesDisabled)(),r="CurrentUserOrganizationConnection"===e.orgs.__typename?e.orgs.items:null,{showError:s}=(0,eb.default)(),c=(0,eu.useRouter)();return!r?.length||o?null:(0,t.jsxs)(eL.MenuSection,{children:[(0,t.jsx)(ew.MenuHeader,{text:"Switch Workspace"}),a?null:(0,t.jsx)(e_,{icon:(0,t.jsx)(Y.Avatar,{size:16,src:e.image,username:e.username,fullName:e.fullName}),label:"Personal",onAction:()=>{n({type:ef.OrgType.Personal}),c.push("/home","/~",{shallow:!1})},right:void 0===i.orgId?(0,t.jsx)($.default,{}):void 0,selected:void 0===i.orgId}),r.map(({org:e,type:o})=>(0,t.jsxs)(ew.BaseMenuItem,{textValue:e.name,onAction:()=>(e=>{if(!e.currentUserRole)return void s("Something went wrong, please try again.");n({type:ef.OrgType.Team,id:e.id,slug:e.slug,orgRole:e.currentUserRole,orgDealContext:e.dealContext});let{home:t}=(0,eF.orgLinks)({slug:e.slug});c.push(t.href,t.as)})(e),children:[(0,t.jsxs)(Z.View,{grow:!0,shrink:!0,row:!0,gap:6,align:"center",children:[(0,t.jsx)(Y.Avatar,{size:16,src:e.image??null,username:e.name,fullName:e.name}),(0,t.jsx)(Q.Text,{translate:"no",children:e.name}),o?(0,t.jsx)(Q.Text,{variant:"small",color:"dimmest",children:(0,eG.orgGroupToDisplayName)(o)}):null]}),e.id===i.orgId?(0,t.jsx)($.default,{}):null]},e.id)),(0,t.jsx)(ew.Separator,{})]})}],246613);var eH=e.i(155119),eK=e.i(759317),eJ=e.i(393428),eY=e.i(308521),eQ=e.i(401036),eX=e.i(841114);e.s(["ThemeItem",0,function(){let{currentTheme:e}=(0,eQ.useTheme)(),{setActiveTheme:i,isSystemTheme:o}=(0,eX.useThemePreference)(),n="Custom";return o?n="System":"replitDark"===e.id?n="Dark":"replitLight"===e.id&&(n="Light"),(0,t.jsxs)(eL.SubmenuTrigger,{children:[(0,t.jsx)(ew.BaseMenuItem,{textValue:"Theme",children:(0,t.jsxs)(Z.View,{align:"center",row:!0,gap:6,justify:"space-between",grow:!0,shrink:!0,children:[(0,t.jsxs)(Z.View,{align:"center",grow:!0,shrink:!0,row:!0,gap:6,children:[(0,t.jsx)(eJ.default,{}),(0,t.jsx)(Q.Text,{multiline:!1,children:"Theme"})]}),(0,t.jsxs)(Z.View,{row:!0,gap:4,align:"center",children:[(0,t.jsx)(Q.Text,{color:"dimmer",children:n}),(0,t.jsx)(E.default,{size:12})]})]})}),(0,t.jsx)(eU.RawPopover,{offset:4,children:(0,t.jsx)(Z.View,{p:4,children:(0,t.jsxs)(ew.Menu,{"aria-label":"Theme",children:[(0,t.jsx)(ew.MenuItem,{label:"Light",icon:(0,t.jsx)(eY.default,{size:16}),onAction:()=>i("replitLight")}),(0,t.jsx)(ew.MenuItem,{label:"Dark",icon:(0,t.jsx)(eK.default,{size:16}),onAction:()=>i("replitDark")}),(0,t.jsx)(ew.MenuItem,{label:"System",icon:(0,t.jsx)(eH.default,{size:16}),onAction:()=>i("system")})]})})})]})}],13465)}]);

//# debugId=3cd09c20-6951-12e1-eced-3e878a022d72
//# sourceMappingURL=08h8525z01zfr.js.map
